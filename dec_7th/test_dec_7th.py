from dec_7th import sum_possible_calibrations, calibration_check


class TestSumPossibleCalibrations:
    def test_func_returns_correct_value_for_test_data(self):
        test_filepath = "dec_7th/test_input_1.txt"
        expected_return = 3749
        assert sum_possible_calibrations(test_filepath) == expected_return


class TestCalibrationCheck:
    def test_func_returns_correct_value_for_simple_true_case(self):
        test_input = [4, [2, 2]]
        expected_return = 4
        assert calibration_check(test_input) == expected_return

    def test_func_returns_false_correctly_for_simple_case(self):
        test_input = [10, [2, 2]]
        expected_return = False
        assert calibration_check(test_input) == expected_return

    def test_func_returns_correct_value_for_complex_true_case(self):
        test_input = [204, [5, 10, 1, 4]]
        expected_return = 204
        assert calibration_check(test_input) == expected_return

    def test_func_returns_correct_value_for_complex_false_case(self):
        test_input = [19, [2, 3, 10]]
        expected_return = False
        assert calibration_check(test_input) == expected_return

    def test_func_can_alternate_between_operators(self):
        test_input = [25, [1, 2, 3, 4, 5]]
        expected_return = 25
        assert calibration_check(test_input) == expected_return

        test_input = [65, [1, 2, 3, 4, 5]]
        expected_return = 65
        assert calibration_check(test_input) == expected_return

    def test_func_can_handle_long_input(self):
        test_input = [
            1048576,
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ]
        expected_return = 1048576
        assert calibration_check(test_input) == expected_return
