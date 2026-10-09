"""Automated checks for Activity 5: French Creek Field Notes.

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
QUESTIONS = ["name", "watch", "lookup"]

SAFE = dict(name="JJ", watch=50, lookup=1)


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
    context = f"readings: {used}, watch={answers['watch']}, day looked up={answers['lookup']}"
    if "FIELD LOG" not in out.upper():
        raise AssertionError(f"no \"FIELD LOG\" line was printed ({context})")
    got = log_value(out, label)
    if got is None:
        raise AssertionError(f'no "{label}" line was printed after FIELD LOG ({context})')
    # A printed list may or may not have spaces after its commas.
    assert got.replace(" ", "") == str(want).upper().replace(" ", ""), (
        f'the "{label}" line said {got}, expected {want} ({context})'
    )
    return out


def test_log_names_you_and_counts_the_readings(capsys):
    expect(capsys, "FIELD LOG", "JJ")
    expect(capsys, "Readings", 7)
    # A different length, so a 7 typed in by hand does not pass.
    expect(capsys, "Readings", 3, readings=[12, 20, 7])


def test_first_and_last_come_from_the_ends(capsys):
    expect(capsys, "First", 31)
    expect(capsys, "Last", 36)
    expect(capsys, "First", 12, readings=[12, 20, 7])
    expect(capsys, "Last", 7, readings=[12, 20, 7])


def test_highest_and_average(capsys):
    expect(capsys, "Highest", 68)
    # Largest in the middle, at the end, and at the very start.
    expect(capsys, "Highest", 20, readings=[12, 20, 7])
    expect(capsys, "Highest", 41, readings=[12, 20, 41])
    expect(capsys, "Highest", 55, readings=[55, 20, 41])
    # 305 // 7 is 43, where 305 / 7 would be 43.571...
    expect(capsys, "Average", 43)
    expect(capsys, "Average", 13, readings=[12, 20, 7])


def test_watch_days_lists_the_days_at_or_above(capsys):
    # Days 3 and 4 (52 and 68) reach a watch level of 50.
    expect(capsys, "Watch days", "[3, 4]", watch=50)
    expect(capsys, "Reached watch", 2, watch=50)
    # A reading exactly at the watch level counts, and days count from 1.
    expect(capsys, "Watch days", "[3]", readings=[10, 20, 30], watch=30)
    expect(capsys, "Watch days", "[]", readings=[10, 20, 30], watch=31)
    expect(capsys, "Watch days", "[1, 2, 3]", readings=[10, 20, 30], watch=10)
    expect(capsys, "Reached watch", 3, readings=[10, 20, 30], watch=10)


def test_day_lookup_counts_from_one(capsys):
    expect(capsys, "Day lookup", 68, lookup=4)
    expect(capsys, "Day lookup", 31, lookup=1)
    expect(capsys, "Day lookup", 7, readings=[12, 20, 7], lookup=3)
    # Days outside the list have no reading.
    expect(capsys, "Day lookup", "none", lookup=0)
    expect(capsys, "Day lookup", "none", readings=[12, 20, 7], lookup=4)
    expect(capsys, "Day lookup", "none", lookup=8)


def test_days_to_fall_below_watch(capsys):
    # 68, 64, 60, 56, 52 are all at or above 50: five days to reach 48.
    expect(capsys, "Days to fall below watch", 5, watch=50)
    # A peak exactly at the watch level takes one day.
    expect(capsys, "Days to fall below watch", 1, readings=[12, 20, 7], watch=20)
    # A peak already below the watch level takes none.
    expect(capsys, "Days to fall below watch", 0, readings=[12, 20, 7], watch=21)
