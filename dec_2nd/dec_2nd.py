# --- Day 2: Red-Nosed Reports ---

# Fortunately, the first location The Historians want to search isn't a long walk from
# the Chief Historian's office.

# While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign
# of the Chief Historian, the engineers there run up to you as soon as they see you.
# Apparently, they still talk about the time Rudolph was saved through molecular synthesis
# from a single electron.

# They're quick to add that - since you're already here - they'd really appreciate your
# help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The
# Historians are waiting for you, but they seem to have already divided into groups that
# are currently searching every corner of the facility. You offer to help with the unusual
# data.

# The unusual data (your puzzle input) consists of many reports, one report per line.
# Each report is a list of numbers called levels that are separated by spaces. For example:

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# This example data contains six reports each containing five levels.

# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor
# safety systems can only tolerate levels that are either gradually increasing or
# gradually decreasing. So, a report only counts as safe if both of the following are true:

#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

# In the example above, the reports can be found safe or unsafe by checking those rules:

#     7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#     1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#     9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#     1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#     8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#     1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

# So, in this example, 2 reports are safe.

# Analyze the unusual data from the engineers. How many reports are safe?

# Your puzzle answer was 624.

# The first half of this puzzle is complete! It provides one gold star: *
# --- Part Two ---

# The engineers are surprised by the low number of safe reports until they realize
# they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor safety
# systems tolerate a single bad level in what would otherwise be a safe report.
# It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level from an
# unsafe report would make it safe, the report instead counts as safe.

# More of the above example's reports are now safe:

#     7 6 4 2 1: Safe without removing any level.
#     1 2 7 8 9: Unsafe regardless of which level is removed.
#     9 7 6 2 1: Unsafe regardless of which level is removed.
#     1 3 2 4 5: Safe by removing the second level, 3.
#     8 6 4 4 1: Safe by removing the third level, 4.
#     1 3 6 7 9: Safe without removing any level.

# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener can remove
# a single level from unsafe reports. How many reports are now safe?

"""
running this file in python will print values for both parts of todays problem
"""


def get_safety_count(filepath, problem_damper):
    """
    this function was re-written so it can solve both parts of todays problem
    it can take problem dampner as an argument, which is 0 in the first part of
    the problem and 1 in the second part
    theoretically it can accept higher values for the problem damper, and thereby
    handle lines with more that one issue
    """
    # get data from file
    with open(filepath) as file:
        file_data = [[int(num) for num in line.split(" ")] for line in file]

    # get count of safe reactors
    safety_count = sum(step_check(line, problem_damper) for line in file_data)

    return safety_count


def step_check(line, problem_damper):
    """
    this function looks at the changes between each element in a given line and returns true if they are
    all gradually ascending or descending. if the problem damper is greater than 0, it can accept that
    many problem values in the line, by calling itself recursively on each possible version of a problematic
    line with a reduced problem damper
    """
    steps = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    if all(0 < step < 4 for step in steps) or all(-4 < step < 0 for step in steps):
        return True
    elif problem_damper > 0:
        return any(
            step_check(line[:i] + line[i + 1 :], problem_damper - 1)
            for i in range(len(line))
        )
    else:
        return False


if __name__ == "__main__":
    print(f"SAFETY COUNT NO DAMPER: {get_safety_count('dec_2nd/input_1.txt', 0)}")
    print(f"SAFETY COUNT WITH DAMPER: {get_safety_count('dec_2nd/input_1.txt', 1)}")
