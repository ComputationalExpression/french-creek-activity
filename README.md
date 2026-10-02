# Activity 5: French Creek Field Notes

|Item |       |
|:----|:------|
|Released |Monday, October 12, in class |
|Due |Wednesday, October 14, 9:50am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

French Creek runs through Meadville on its way to the Allegheny River, and it holds more fish
species and more freshwater mussel species than any other creek in Pennsylvania. Allegheny
faculty and students have been studying its watershed for fifty years. Your program reads a
week of gauge readings out of that work and reports on them.

Everything here comes from the Week 6 and Week 7 lists sessions and the weeks before them. If a step confuses you,
please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this activity you should be able to:

* read how many items a list holds with `len`
* pick an item out of a list by position, including the last one
* visit every item of a list with `for item in a_list`
* set a variable before a loop and change it inside the loop, to count and to compare
* choose between `/` and `//` for the result you want

## The problem

The list of readings is provided at the top of `src/main.py`:

```python
levels = [31, 34, 52, 68, 45, 39, 36]
```

**Your program has to work for any list of readings, not just this one.** Take every number
it reports from the list itself. A number counted by eye and typed in is right until the list
changes, and the automated checks run your program against a different list.

Your program asks for a name and a watch level, prints the first and last readings, walks the
list once, and ends with a field log holding six values:

|Value |Where it comes from |
|:-----|:-------------------|
|`Readings` |How many items the list holds |
|`First` |The reading at position `0` |
|`Last` |The reading at the last position, whatever the length |
|`Highest` |The largest reading |
|`Reached watch` |How many readings are at or above the watch level |
|`Average` |The total divided by how many readings, as a whole number |

A reading exactly at the watch level counts as having reached it. The average uses `//`, so
`305` across seven readings is `43` rather than `43.57142857142857`.

One pass down the list is enough for the last three values. Counting, comparing, and totaling
can all happen on the same trip.

### Example run

```text
$ uv run python src/main.py
==================================================
FRENCH CREEK FIELD NOTES
==================================================
What is your name? JJ
What is the watch level this week? 50
First reading: 31
Last reading: 36
Reading: 31
Reading: 34
Reading: 52
Reading: 68
Reading: 45
Reading: 39
Reading: 36

==================================================
FIELD LOG: JJ
==================================================
Readings: 7
First: 31
Last: 36
Highest: 68
Reached watch: 2
Average: 43
```

Your wording is yours. The checks read only the field log at the end, they forgive extra
spaces and letter case, and any of the three ways to print a value passes:
`print("Highest:", highest)`, `print("Highest: " + str(highest))`, or
`print(f"Highest: {highest}")`.

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it as you go, rather than
writing all of it and running it once:

```text
uv run python src/main.py
```

Put your name on the `Author:` line at the top of the file, and delete each `TODO` marker as
you finish that step.

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. What is graded is the attempt, not whether every value comes out right.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |At least half of the activity is done |
|**Partial** |Less than half is done, but something beyond the starter was committed |
|**Incomplete** |Nothing was changed |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository rather than from inside `src`:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command. Run it: the last lines name the log line that came
out wrong, what it said, what was expected, and the readings that were used.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded.

**In the terminal:**

```text
git add src/main.py
git commit -m "Complete the French Creek field notes"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it, which is `git add`
2. Type a message in the box at the top, then click the checkmark, which is `git commit`
3. Click **Sync Changes** (or the up arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
