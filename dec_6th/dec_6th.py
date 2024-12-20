# --- Day 6: Guard Gallivant ---

# The Historians use their fancy device again, this time to whisk you all
# away to the North Pole prototype suit manufacturing lab... in the year
# 1518! It turns out that having direct access to history is very
# convenient for a group of historians.

# You still have to be careful of time paradoxes, and so it will be
# important to avoid anyone from 1518 while The Historians search for the
# Chief. Unfortunately, a single guard is patrolling this part of the lab.

# Maybe you can work out where the guard will go ahead of time so that
# the Historians can search safely?

# You start by making a map (your puzzle input) of the situation. For
# example:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

# The map shows the current position of the guard with ^ (to indicate the
# guard is currently facing up from the perspective of the map). Any
# obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves
# repeatedly following these steps:

#     If there is something directly in front of you, turn right 90 degrees.
#     Otherwise, take a step forward.

# Following the above protocol, the guard moves up several times until she
# reaches an obstacle (in this case, a pile of failed suit prototypes):

# ....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...

# Because there is now an obstacle in front of the guard, she turns right
# before continuing straight in her new facing direction:

# ....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...

# Reaching another obstacle (a spool of several very long polymers), she
# turns right again and continues downward:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#...

# This process continues for a while, but the guard eventually leaves the
# mapped area (after walking past a tank of universal solvent):

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v..

# By predicting the guard's route, you can determine which specific
# positions in the lab will be in the patrol path. Including the guard's
# starting position, the positions visited by the guard before leaving the
# area are marked with an X:

# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..

# In this example, the guard will visit 41 distinct positions on your map.

# Predict the path of the guard. How many distinct positions will the
# guard visit before leaving the mapped area?

# --- Part Two ---

# While The Historians begin working around the guard's patrol route, you
# borrow their fancy device and step outside the lab. From the safety of a
# supply closet, you time travel through the last few months and record the
# nightly status of the lab's guard post on the walls of the closet.

# Returning after what seems like only a few seconds to The Historians, they
# explain that the guard's patrol area is simply too large for them to safely
# search the lab without getting caught.

# Fortunately, they are pretty sure that adding a single new obstruction won't
# cause a time paradox. They'd like to place the new obstruction in such a way
# that the guard will get stuck in a loop, making the rest of the lab safe to
# search.

# To have the lowest chance of creating a time paradox, The Historians would
# like to know all of the possible positions for such an obstruction. The new
# obstruction can't be placed at the guard's starting position - the guard is
# there right now and would notice.

# In the above example, there are only 6 different positions where a new
# obstruction would cause the guard to get stuck in a loop. The diagrams of
# these six situations use O to mark the new obstruction, | to show a position
# where the guard moves up/down, - to show a position where the guard moves
# left/right, and + to show a position where the guard moves both up/down and
# left/right.

# Option one, put a printing press next to the guard's starting position:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...

# Option two, put a stack of failed suit prototypes in the bottom right quadrant
# of the mapped area:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...

# Option three, put a crate of chimney-squeeze prototype fabric next to the standing
# desk in the bottom right quadrant:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...

# Option four, put an alchemical retroencabulator near the bottom left corner:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...

# Option five, put the alchemical retroencabulator a bit to the right instead:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...

# Option six, put a tank of sovereign glue right next to the tank of universal solvent:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..

# It doesn't really matter what you choose to use as an obstacle so long as you and The
# Historians can put it into position without the guard noticing. The important thing is
# having enough options that you can find one that minimizes time paradoxes, and in this
# example, there are 6 different positions you could choose.

# You need to get the guard stuck in a loop by adding a single new obstruction. How many
# different positions could you choose for this obstruction?


"""running this file in python will print the solutions to both parts of todays problem"""


"""it is necessary to raise the recusrion limit in order to complete the problem with my chosen
approach. this is was done carefully and with thought in mind to the code being used and the limited
potential for issues to arise. if you run this program on your own input, you may find it necessary
raise the limit slightly, as my own solution took aproximately 4.4k iterations and thus a 5k+ solution 
is not implausible"""
import sys

sys.setrecursionlimit(5000)


def count_spaces(filepath):
    """this function counts the number of unique spaces travelled on the map. it starts by calling get_start
    and get_obstacles to find basic information about the map, and then calls get_path to recursively trace
    the path. get_path returns a list of steps taken on the path, but these are not the same as unique spaces
    visited as get_path distinguishes between direction faced where count spaces does not. therefore we take
    only the first two elements of each step to only get coordinates, use set() to get the unique elements,
    and return the length"""

    with open(filepath) as file:
        initial_map = [[char for char in line if char != "\n"] for line in file]

    map_size = len(initial_map)
    obstacles = get_obstacles(initial_map)
    start = get_start(initial_map)

    path = get_path(map_size, obstacles, start)

    spaces = set([step[:2] for step in path])
    return len(spaces)


def get_path(map_size, obstacles, path):
    """this function takes information about the map and recursively traces the path until it either
    leaves the map"""

    # the bearing is the last element in the path
    bearing = path[-1]

    # calulate the next step based on current bearing
    if bearing[2] == "^":
        next_step = (bearing[0] - 1, bearing[1], "^")
    elif bearing[2] == "v":
        next_step = (bearing[0] + 1, bearing[1], "v")
    elif bearing[2] == ">":
        next_step = (bearing[0], bearing[1] + 1, ">")
    elif bearing[2] == "<":
        next_step = (bearing[0], bearing[1] - 1, "<")

    # if the next step hits and obstacle, instead keep the location of the current bearing and change facing
    if next_step[:2] in obstacles:
        if next_step[2] == "^":
            next_step = (bearing[0], bearing[1], ">")
        elif next_step[2] == ">":
            next_step = (bearing[0], bearing[1], "v")
        elif next_step[2] == "v":
            next_step = (bearing[0], bearing[1], "<")
        elif next_step[2] == "<":
            next_step = (bearing[0], bearing[1], "^")

    # if the next step would leave the map return the current path
    if next_step[0] in [-1, map_size] or next_step[1] in [-1, map_size]:
        return path

    # otherwise call the function recursively with the next step added to the path
    else:
        path.append(next_step)
        return get_path(map_size, obstacles, path)


def get_obstacles(initial_map):
    """this function uses a list comprehension to find the obstacles on the map and returns
    a list of their coordinates"""
    return [
        (row, column)
        for row in range(len(initial_map))
        for column in range(len(initial_map[row]))
        if initial_map[row][column] == "#"
    ]


def get_start(initial_map):
    """this function uses a list comprehension to find the location and facing of the start
    location. it returns as a list so get_path can treat it as a path with only one step
    """
    return [
        (row, column, initial_map[row][column])
        for row in range(len(initial_map))
        for column in range(len(initial_map[row]))
        if initial_map[row][column] in ["^", "v", ">", "<"]
    ]


"""this was my first approach at part 2 but it takes way to long. given that my first solution
was about 4.4k unique spaces, I imagine that it is running around that many version of get_path,
which means perhaps 2e+7 steps to follow"""

# def count_loops(filepath):
#     """this function checks generates the path as above, but now looks for ways in which the path
#     could be turned into a loop by adding an obstacle. to do this, it calls loop_check on every
#     step on the original path and simulates what would happen if the next step was facing an obstacle.
#     loop_check returns True if the new obstacle forms a loop and False otherise, so a sum of these
#     returns gives a count of the number of possible loops
#     """
#     with open(filepath) as file:
#         initial_map = [[char for char in line if char != "\n"] for line in file]

#     map_size = len(initial_map)
#     obstacles = get_obstacles(initial_map)
#     start = get_start(initial_map)

#     path = get_path(map_size, obstacles, start)

#     return sum(
#         [
#             loop_check(map_size, obstacles, path[:divergence_point], divergence_point)
#             for divergence_point in range(1, len(path))
#         ]
#     )

# def loop_check(map_size, obstacles, path, divergence_point):
#     """this function works similarly to get_path but instead works simualtes adding an
#     obstacle on its first invocation and then calls itself recursively to follow the
#     new path and check if it forms a loop"""
#     # bearing is the last step in the path
#     bearing = path[-1]

#     # check if this is the point at which the path diverges. if so, act as if there is an obstacle
#     if divergence_point == len(path):
#         if bearing[2] == "^":
#             next_step = (bearing[0], bearing[1], ">")
#         elif bearing[2] == ">":
#             next_step = (bearing[0], bearing[1], "v")
#         elif bearing[2] == "v":
#             next_step = (bearing[0], bearing[1], "<")
#         elif bearing[2] == "<":
#             next_step = (bearing[0], bearing[1], "^")

#     # if this is not the divergence point, continue as normal in following the path
#     else:
#         # calulate the next step based on current bearing
#         if bearing[2] == "^":
#             next_step = (bearing[0] - 1, bearing[1], "^")
#         elif bearing[2] == "v":
#             next_step = (bearing[0] + 1, bearing[1], "v")
#         elif bearing[2] == ">":
#             next_step = (bearing[0], bearing[1] + 1, ">")
#         elif bearing[2] == "<":
#             next_step = (bearing[0], bearing[1] - 1, "<")

#         # if the next step hits and obstacle, instead keep the location of the current bearing and change facing
#         if next_step[:2] in obstacles:
#             if next_step[2] == "^":
#                 next_step = (bearing[0], bearing[1], ">")
#             elif next_step[2] == ">":
#                 next_step = (bearing[0], bearing[1], "v")
#             elif next_step[2] == "v":
#                 next_step = (bearing[0], bearing[1], "<")
#             elif next_step[2] == "<":
#                 next_step = (bearing[0], bearing[1], "^")

#     # if the next step would leave the map return the current path
#     if next_step[0] in [-1, map_size] or next_step[1] in [-1, map_size]:
#         return False
#     elif next_step in path:
#         return True

#     # otherwise call the function recursively with the next step added to the path
#     else:
#         path.append(next_step)
#         return loop_check(map_size, obstacles, path, divergence_point)


if __name__ == "__main__":
    print(f"SPACES TRAVELLED: {count_spaces('dec_6th/input_1.txt')}")
