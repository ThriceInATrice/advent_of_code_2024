from dec_8th import (
    get_antinode_count,
    get_antenas,
    get_antena_pairs,
    get_antinodes,
    get_harmonic_antinode_count,
)


class TestGetAntinodeCount:
    def test_func_counts_antipodes_correctly(self):
        test_filepath = "dec_8th/test_input_1.txt"
        expected_return = 2
        assert get_antinode_count(test_filepath) == expected_return

    def test_func_ignores_antipodes_outside_the_grid(self):
        test_filepath = "dec_8th/test_input_2.txt"
        expected_return = 4
        assert get_antinode_count(test_filepath) == expected_return

    def test_func_can_handle_different_symbols(self):
        test_filepath = "dec_8th/test_input_3.txt"
        expected_return = 14
        assert get_antinode_count(test_filepath) == expected_return

    def test_func_counts_double_antipodes_only_once(self):
        test_filepath = "dec_8th/test_input_4.txt"
        expected_return = 3
        assert get_antinode_count(test_filepath) == expected_return

    def test_func_can_tell_the_difference_between_capitals_and_non_capitals(self):
        test_filepath = "dec_8th/test_input_5.txt"
        expected_return = 0
        assert get_antinode_count(test_filepath) == expected_return


class TestGetAntenas:
    def test_func_finds_antenas_in_one_line(self):
        test_input = ["aa"]
        expected_return = [[(0, 0), (0, 1)]]
        assert get_antenas(test_input) == expected_return

    def test_func_can_handle_more_than_one_symbol(self):
        test_input = ["ab"]
        expected_return = [[(0, 0)], [(0, 1)]]
        assert get_antenas(test_input) == expected_return

    def test_func_can_differentiate_capitals(self):
        test_input = ["a.", "Aa"]
        expected_return = [[(1, 0)], [(0, 0), (1, 1)]]
        assert get_antenas(test_input) == expected_return

    def test_func_can_handle_multiple_lines(self):
        test_input = ["a..", "aa.", "..a"]
        expected_return = [[(0, 0), (1, 0), (1, 1), (2, 2)]]
        assert get_antenas(test_input) == expected_return

    def test_func_on_complex_example(self):
        test_input = ["b.1.a", "a....", "..1..", ".b...", ".1.b."]
        expected_return = [
            [(0, 2), (2, 2), (4, 1)],
            [(0, 4), (1, 0)],
            [(0, 0), (3, 1), (4, 3)],
        ]
        assert get_antenas(test_input) == expected_return


class TestGetAntenaPairs:
    def test_func_returns_empty_list_for_single_coord(self):
        test_input = [[(0, 0)]]
        expected_return = []
        assert get_antena_pairs(test_input) == expected_return

    def test_func_handles_pair_of_coords(self):
        test_input = [[(0, 0), (1, 1)]]
        expected_return = [((0, 0), (1, 1)), ((1, 1), (0, 0))]
        assert get_antena_pairs(test_input) == expected_return

    def test_func_returns_correct_pairs(self):
        test_input = [[(0, 0), (1, 1)], [(1, 2), (3, 4), (5, 6)]]
        expected_return = [
            ((0, 0), (1, 1)),
            ((1, 1), (0, 0)),
            ((1, 2), (3, 4)),
            ((1, 2), (5, 6)),
            ((3, 4), (1, 2)),
            ((3, 4), (5, 6)),
            ((5, 6), (1, 2)),
            ((5, 6), (3, 4)),
        ]
        assert get_antena_pairs(test_input) == expected_return


class TestGetAntinodes:
    def test_func_returns_correct_antinodes_for_single_pair(self):
        test_input = [((0, 1), (0, 2)), ((0, 2), (0, 1))]
        expected_return = {(0, 0), (0, 3)}
        assert get_antinodes(test_input, 5) == expected_return

    def test_func_ignores_antinodes_outside_grid(self):
        test_input = [((0, 1), (0, 2)), ((0, 2), (0, 1))]
        expected_return = {(0, 0)}
        assert get_antinodes(test_input, 3) == expected_return

    def test_func_counts_overlaps_only_once(self):
        test_input = [
            ((0, 1), (0, 2)),
            ((0, 2), (0, 1)),
            ((1, 0), (2, 0)),
            ((2, 0), (1, 0)),
        ]
        expected_return = {(0, 0), (0, 3), (3, 0)}
        assert get_antinodes(test_input, 5) == expected_return


class TestGetHarmnicAntinodes:
    def test_func_returns_correct_value_for_simple_case(self):
        test_filepath = "dec_8th/test_input_6.txt"
        expected_return = 9
        assert get_harmonic_antinode_count(test_filepath) == expected_return

    def test_func_returns_correct_value_for_complex_case(self):
        test_filepath = "dec_8th/test_input_3.txt"
        expected_return = 34
        assert get_harmonic_antinode_count(test_filepath) == expected_return
