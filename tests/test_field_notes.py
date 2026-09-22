"""Automated checks for Activity 3: French Creek Field Notes.

Every check reads the field log at the end of the run, never the lines
printed along the way, so the wording is yours. Log values are matched
loosely: any amount of whitespace, any letter case, and the colon is
optional, so `print("Highest:", highest)`, `print("Highest: " + str(highest))`
and `print(f"Highest: {highest}")` all read the same.

Most checks replace the provided list with a different one before running, so
a number that was counted by eye and typed in passes only for the list it was
counted from. Take every number from the list itself.

When a check fails, the assertion message says which log line came out wrong,
what it said, what was expected, and the readings that were used.
"""

import re
from unittest.mock import patch

import main
from main import main as run_main

# The order the starter asks its questions.
QUESTIONS = ["name", "watch"]

SAFE = dict(name="JJ", watch=50)


def run(capsys, readings=None, **changes):
    """Run main() once, optionally against a different list of readings."""
    answers = {**SAFE, **changes}
    typed = [str(answers[q]) for q in QUESTIONS]
    original = main.levels
    if readings is not None:
        main.levels = list(readings)
    try:
        with patch("builtins.input", side_effect=typed):
            run_main()
    finally:
        main.levels = original
    out, err = capsys.readouterr()
    assert err == "", "the program wrote to the error stream:\n" + err
    return out, answers, list(readings) if readings is not None else list(original)


def log_value(out, label):
    """Return the value printed after `label` in the field log, normalized."""
    start = out.upper().find("FIELD LOG")
    if start < 0:
        return None
    words = r"\s+".join(re.escape(word) for word in label.split())
    match = re.search(rf"{words}\s*:?\s*([^\n]*)", out[start:], re.IGNORECASE)
    if match is None:
        return None
    return " ".join(match.group(1).split()).upper().rstrip(".! ")


def expect(capsys, label, want, readings=None, **changes):
    """Run once and check that the field log line `label` says `want`."""
    out, answers, used = run(capsys, readings=readings, **changes)
    context = f"readings: {used}, watch={answers['watch']}"
    if "FIELD LOG" not in out.upper():
        raise AssertionError(f"no \"FIELD LOG\" line was printed ({context})")
    got = log_value(out, label)
    if got is None:
        raise AssertionError(f'no "{label}" line was printed after FIELD LOG ({context})')
    assert got == str(want), f'the "{label}" line said {got}, expected {want} ({context})'
    return out


def test_program_runs_and_log_names_you(capsys):
    expect(capsys, "FIELD LOG", "JJ")


def test_readings_counts_the_list(capsys):
    expect(capsys, "Readings", 7)
    # A different length, so a 7 typed in by hand does not pass.
    expect(capsys, "Readings", 3, readings=[12, 20, 7])


def test_first_and_last_come_from_the_ends(capsys):
    expect(capsys, "First", 31)
    expect(capsys, "Last", 36)
    expect(capsys, "First", 12, readings=[12, 20, 7])
    expect(capsys, "Last", 7, readings=[12, 20, 7])


def test_highest_is_the_largest_reading(capsys):
    expect(capsys, "Highest", 68)
    # Largest in the middle, at the end, and at the very start.
    expect(capsys, "Highest", 20, readings=[12, 20, 7])
    expect(capsys, "Highest", 41, readings=[12, 20, 41])
    expect(capsys, "Highest", 55, readings=[55, 20, 41])


def test_reached_watch_counts_at_or_above(capsys):
    # 52 and 68 reach a watch level of 50.
    expect(capsys, "Reached watch", 2, watch=50)
    # A reading exactly at the watch level counts.
    expect(capsys, "Reached watch", 1, readings=[10, 20, 30], watch=30)
    expect(capsys, "Reached watch", 0, readings=[10, 20, 30], watch=31)
    expect(capsys, "Reached watch", 3, readings=[10, 20, 30], watch=10)


def test_average_is_a_whole_number(capsys):
    # 305 // 7 is 43, where 305 / 7 would be 43.571...
    expect(capsys, "Average", 43)
    expect(capsys, "Average", 13, readings=[12, 20, 7])
