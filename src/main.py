"""French Creek Field Notes.

CMPSC 100: Computational Expression, Activity 5

A week of gauge readings from French Creek, kept in one list. Read the list,
walk it, look up one day, and work out how long the creek takes to fall back
below the watch level.

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

    # TODO 3: ask which day to look up, save it to a variable called `lookup`,
    # and convert it to an int

    # TODO 4: print the first reading and the last reading. The first is at
    # position 0. The last is at position len(levels) - 1, whatever the length

    # TODO 5: set four variables to start from: `highest` to levels[0],
    # `total` to 0, `watch_days` to an empty list, and `day` to 0

    # TODO 6: write one for loop over `levels`. On every trip:
    # add 1 to `day`, then print the day and its reading
    # if the reading is greater than or equal to `watch`, append `day` to `watch_days`
    # if the reading is greater than `highest`, save it to `highest`
    # add the reading to `total`

    # TODO 7: if `lookup` is at least 1 and at most the number of readings
    # (two comparisons joined with and), save the reading for that day to
    # `looked_up`. Day 1 is position 0. Otherwise save "none" to `looked_up`

    # TODO 8: the creek falls 4 a day from its highest reading. Set `falling`
    # to `highest` and `days_to_fall` to 0. While `falling` is greater than or
    # equal to `watch`, subtract 4 from `falling` and add 1 to `days_to_fall`

    # TODO 9: print the field log, one line each, in this order:
    # "FIELD LOG: {name}", then a line of 50 "=" characters, then
    # "Readings: {how many readings are in the list}",
    # "First: {the first reading}", "Last: {the last reading}",
    # "Highest: {highest}",
    # "Average: {total divided by how many readings, using //}",
    # "Watch days: {watch_days}", "Reached watch: {how many items watch_days holds}",
    # "Day lookup: {looked_up}", and "Days to fall below watch: {days_to_fall}"
    # Print each value any way you like: commas, + with str(), or an f-string


if __name__ == "__main__":
    main()
