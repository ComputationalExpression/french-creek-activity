"""French Creek Field Notes.

CMPSC 100: Computational Expression, Activity 5

A week of gauge readings from French Creek, kept in one list. Read the list,
walk it, and report on it.

The list below is provided. Your program should work for any list of
readings, so take every number it reports from the list itself rather than
counting by eye.

Author: TODO
"""

levels = [31, 34, 52, 68, 45, 39, 36]


def main():
    print("=" * 50)
    print("FRENCH CREEK FIELD NOTES")
    print("=" * 50)

    # TODO 1: ask the user's name, save it to a variable called `name`

    # TODO 2: ask what the watch level is for this week, save it to a variable
    # called `watch`, and convert it to an int

    # TODO 3: print the first reading and the last reading. The first is at
    # position 0. The last is at position len(levels) - 1, whatever the length

    # TODO 4: set three variables to start counting from: `reached` to 0,
    # `highest` to levels[0], and `total` to 0

    # TODO 5: write one for loop over `levels`. On every trip:
    # print the reading
    # if it is greater than or equal to `watch`, add 1 to `reached`
    # if it is greater than `highest`, save it to `highest`
    # add the reading to `total`

    # TODO 6: print the field log, one line each, in this order:
    # "FIELD LOG: {name}", then a line of 50 "=" characters, then
    # "Readings: {how many readings are in the list}",
    # "First: {the first reading}", "Last: {the last reading}",
    # "Highest: {highest}", "Reached watch: {reached}", and
    # "Average: {total divided by how many readings, using //}"
    # Print each value any way you like: commas, + with str(), or an f-string


if __name__ == "__main__":
    main()
