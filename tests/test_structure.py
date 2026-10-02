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


def test_len_is_called_and_the_list_is_indexed():
    called = [
        n for n in nodes(ast.Call)
        if isinstance(n.func, ast.Name) and n.func.id == "len"
    ]
    assert called, "found no call to len(...): how many readings there are comes from the list, not from a number typed in"
    assert nodes(ast.Subscript), "found no indexing like levels[0]: the first and last readings are picked by position"


def test_a_for_loop_over_the_list():
    found = [
        loop for loop in nodes(ast.For)
        if isinstance(loop.iter, ast.Name) and loop.iter.id == "levels"
    ]
    assert found, "found no `for ... in levels:` loop: one pass down the list does the counting"
