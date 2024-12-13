from dec_6th import (
    count_spaces,
    get_start,
    get_obstacles,
    get_path,
    #count_loops,
    #loop_check,
)


class TestCountSpaces:
    def test_func_returns_correct_value_for_test_data(self):
        test_filepath = "dec_6th/test_input_1.txt"
        expected_return = 41
        assert count_spaces(test_filepath) == expected_return


# class TestCountLoops:
#     def test_count_loops_returns_correct_loop_count_for_test_input(self):
#         test_filepath = "dec_6th/test_input_1.txt"
#         expected_return = 7
#         assert count_loops(test_filepath) == expected_return


class TestGetStart:
    def test_func_can_find_north_facing_start(self):
        test_map = [[".", ".", "."], ["^", ".", "."], [".", ".", "."]]
        expected_return = [(1, 0, "^")]
        assert get_start(test_map) == expected_return

    def test_func_can_find_south_facing_start(self):
        test_map = [[".", ".", "."], [".", ".", "."], ["v", ".", "."]]
        expected_return = [(2, 0, "v")]
        assert get_start(test_map) == expected_return

    def test_func_can_find_east_facing_start(self):
        test_map = [[".", ">", "."], [".", ".", "."], [".", ".", "."]]
        expected_return = [(0, 1, ">")]
        assert get_start(test_map) == expected_return

    def test_func_can_find_west_facing_start(self):
        test_map = [[".", ".", "."], [".", ".", "<"], ["#", ".", "."]]
        expected_return = [(1, 2, "<")]
        assert get_start(test_map) == expected_return


class TestGetObstacles:
    def test_func_can_find_single_obstacle(self):
        test_map = [[".", ".", "."], [".", "#", "."], ["#", ".", "."]]
        expected_return = [(1, 1), (2, 0)]
        assert get_obstacles(test_map) == expected_return

    def test_func_can_find_multiple_obstacle(self):
        test_map = [[".", ".", "#"], [".", "#", "."], ["#", "#", "."]]
        expected_return = [(0, 2), (1, 1), (2, 0), (2, 1)]
        assert get_obstacles(test_map) == expected_return


class TestGetPath:
    def test_func_can_find_basic_path(self):
        test_map_for_visalisation_only = [
            [".", ".", "#", "."],
            [".", ".", "^", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
        ]
        map_size = 4
        obstacles = [(0, 2)]
        start = [(1, 2, "^")]
        expected_return = [(1, 2, "^"), (1, 2, ">"), (1, 3, ">")]
        assert get_path(map_size, obstacles, start) == expected_return

    def test_func_can_find_path_with_multiple_obstacles(self):
        test_map_for_visalisation_only = [
            [".", "#", ".", "."],
            [".", ".", "#", "."],
            [".", ".", ".", "."],
            ["#", ".", "<", "."],
        ]
        map_size = 4
        obstacles = [(0, 1), (1, 2), (3, 0)]
        start = [(3, 2, "<")]
        expected_return = [
            (3, 2, "<"),
            (3, 1, "<"),
            (3, 1, "^"),
            (2, 1, "^"),
            (1, 1, "^"),
            (1, 1, ">"),
            (1, 1, "v"),
            (2, 1, "v"),
            (3, 1, "v"),
        ]
        assert get_path(map_size, obstacles, start) == expected_return


# class TestLoopCheck:
#     # def test_func_returns_false_when_adding_an_obstacle_does_not_form_a_loop(self):

#     #     pass

#     def test_func_first_example_from_test_data(self):
#         with open("dec_6th/test_input_1.txt") as file:
#             initial_map = [[char for char in line if char != "\n"] for line in file]
#         map_size = len(initial_map)
#         obstacles = get_obstacles(initial_map)
#         start = get_start(initial_map)
#         path = get_path(map_size, obstacles, start)
#         divergence_point = 35
#         expected_return = True
#         assert (
#             loop_check(map_size, obstacles, path, divergence_point) == expected_return
#         )
