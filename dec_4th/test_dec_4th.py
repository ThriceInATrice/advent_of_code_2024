from dec_4th import get_descending_diagonals, get_ascending_diagonals, get_xmas_count


class TestGetDiagonals:
    def test_get_descending_diagonals_returns_correct_diagonals(self):
        char_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_return = [[1, 5, 9], [2, 6], [4, 8], [3], [7]]
        assert all(
            item in expected_return for item in get_descending_diagonals(char_matrix)
        )
        assert all(
            item in get_descending_diagonals(char_matrix) for item in expected_return
        )

    def test_get_ascending_diagonals_returns_correct_diagonals(self):
        char_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_return = [[1], [4, 2], [7, 5, 3], [8, 6], [9]]
        assert all(
            item in expected_return for item in get_ascending_diagonals(char_matrix)
        )
        assert all(
            item in get_ascending_diagonals(char_matrix) for item in expected_return
        )


class TestGetXmasCount:
    def test_get_xmas_count_returns_correct_value_for_test_input_1(self):
        test_file_path = "dec_4th/test_input_1.txt"
        expect_return = 18
        assert get_xmas_count(test_file_path) == expect_return
