# --- Day 4: Ceres Search ---

# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....

# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX

# Take a look at the little Elf's word search. How many times does XMAS appear?

# --- Part Two ---

# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S

# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........

# In this example, an X-MAS appears 9 times.

# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


"""
running this file in python will print values for both parts of todays problem
"""

from pprint import pprint
import re


def get_xmas_count(filepath):
    """this function counts the numbers of times the XMAS appears in a grid of characters,
    including forwards, backwards, upwards, downwards, and diagonal in all directions"""

    with open(filepath) as file:
        char_matrix = [[char for char in line if char in "XMAS"] for line in file]

    horizontal_lines = ["".join(row) for row in char_matrix]

    vertical_lines = [
        "".join(column)
        for column in [[row[i] for row in char_matrix] for i in range(len(char_matrix))]
    ]

    descending_diagonals = [
        "".join(diagonal) for diagonal in get_descending_diagonals(char_matrix)
    ]
    ascending_diagonals = [
        "".join(diagonal) for diagonal in get_ascending_diagonals(char_matrix)
    ]

    return sum(
        [
            sum([len(re.findall("XMAS", line)) for line in horizontal_lines]),
            sum([len(re.findall("SAMX", line)) for line in horizontal_lines]),
            sum([len(re.findall("XMAS", line)) for line in vertical_lines]),
            sum([len(re.findall("SAMX", line)) for line in vertical_lines]),
            sum([len(re.findall("XMAS", line)) for line in descending_diagonals]),
            sum([len(re.findall("SAMX", line)) for line in descending_diagonals]),
            sum([len(re.findall("XMAS", line)) for line in ascending_diagonals]),
            sum([len(re.findall("SAMX", line)) for line in ascending_diagonals]),
        ]
    )


def get_descending_diagonals(char_matrix):
    diagonals = []
    for start in [(0, i) for i in range(len(char_matrix))] + [
        (i, 0) for i in range(1, len(char_matrix))
    ]:
        y, x = start
        line = []
        while 0 <= x < len(char_matrix) and 0 <= y < len(char_matrix):
            line.append(char_matrix[y][x])
            x += 1
            y += 1
        diagonals.append(line)
    return diagonals


def get_ascending_diagonals(char_matrix):
    diagonals = []
    for start in [(i, 0) for i in range(len(char_matrix) - 1)] + [
        (len(char_matrix) - 1, i) for i in range(len(char_matrix))
    ]:
        y, x = start
        line = []
        while 0 <= x < len(char_matrix) and 0 <= y < len(char_matrix):
            line.append(char_matrix[y][x])
            x += 1
            y -= 1
        diagonals.append(line)
    return diagonals


if __name__ == "__main__":
    pprint(get_xmas_count("dec_4th/input_1.txt"))
