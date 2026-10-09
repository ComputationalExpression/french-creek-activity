"""Structure checks for Activity 5: French Creek Field Notes.

These read `src/main.py` as Python, not as text, so the words in the TODO
comments do not count. Only real statements do.
"""

import ast
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent / "src" / "main.py"


def tree():
    return ast.parse(SOURCE.read_text(encoding="utf-8"))


def nodes(kind):
    return [n for n in ast.walk(tree()) if isinstance(n, kind)]


def test_a_for_loop_over_the_list_and_a_while_loop():
    found = [
        loop for loop in nodes(ast.For)
        if isinstance(loop.iter, ast.Name) and loop.iter.id == "levels"
    ]
    assert found, "found no `for ... in levels:` loop: one pass down the list does the counting"
    assert nodes(ast.While), "found no while loop: the days to fall below watch are counted with one"


def test_append_and_a_two_sided_check():
    appended = [
        n for n in nodes(ast.Call)
        if isinstance(n.func, ast.Attribute) and n.func.attr == "append"
    ]
    assert appended, "found no call to .append(...): watch_days is built one day at a time"
    joined = [n for n in nodes(ast.BoolOp) if isinstance(n.op, ast.And)]
    chained = [n for n in nodes(ast.Compare) if len(n.ops) == 2]
    assert joined or chained, (
        "found no two comparisons joined with and: the day looked up has to be "
        "at least 1 and at most len(levels)"
    )
