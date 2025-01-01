from dec_7th import (
    get_calibration_sum,
    calibration_check,
)


class TestGetCalibrationSum:
    def test_func_on_exaxmple_data_using_only_mult_and_add(self):
        test_filepath = "dec_7th/test_input_1.txt"
        test_operations = ["mult", "add"]
        expected_return = 3749
        assert get_calibration_sum(test_filepath, test_operations) == expected_return

    def test_func_on_exaxmple_data_using_mult_add_and_concat(self):
        test_filepath = "dec_7th/test_input_1.txt"
        test_operations = ["mult", "add", "concat"]
        expected_return = 11387
        assert get_calibration_sum(test_filepath, test_operations) == expected_return


class TestCalibrationCheck2:
    def test_func_on_test_line_1_with_mult_and_add(self):
        test_input = [190, [10, 19]]
        test_operations = ["mult", "add"]
        expected_return = 190
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_2_with_mult_and_add(self):
        test_input = [3267, [81, 40, 27]]
        test_operations = ["mult", "add"]
        expected_return = 3267
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_3_with_mult_and_add(self):
        test_input = [83, [17, 5]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_4_with_mult_and_add(self):
        test_input = [156, [15, 6]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_5_with_mult_and_add(self):
        test_input = [7290, [6, 8, 6, 15]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_6_with_mult_and_add(self):
        test_input = [161011, [16, 10, 13]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_7_with_mult_and_add(self):
        test_input = [192, [17, 8, 14]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_8_with_mult_and_add(self):
        test_input = [21037, [9, 7, 18, 13]]
        test_operations = ["mult", "add"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_9_with_mult_and_add(self):
        test_input = [292, [11, 6, 16, 20]]
        test_operations = ["mult", "add"]
        expected_return = 292
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_1_with_mult_add_and_concat(self):
        test_input = [190, [10, 19]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 190
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_2_with_mult_add_and_concat(self):
        test_input = [3267, [81, 40, 27]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 3267
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_3_with_mult_add_and_concat(self):
        test_input = [83, [17, 5]]
        test_operations = ["mult", "add", "concat"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_4_with_mult_add_and_concat(self):
        test_input = [156, [15, 6]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 156
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_5_with_mult_add_and_concat(self):
        test_input = [7290, [6, 8, 6, 15]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 7290
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_6_with_mult_add_and_concat(self):
        test_input = [161011, [16, 10, 13]]
        test_operations = ["mult", "add", "concat"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_7_with_mult_add_and_concat(self):
        test_input = [192, [17, 8, 14]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 192
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_8_with_mult_add_and_concat(self):
        test_input = [21037, [9, 7, 18, 13]]
        test_operations = ["mult", "add", "concat"]
        expected_return = False
        assert calibration_check(test_input, test_operations) == expected_return

    def test_func_on_test_line_9_with_mult_add_and_concat(self):
        test_input = [292, [11, 6, 16, 20]]
        test_operations = ["mult", "add", "concat"]
        expected_return = 292
        assert calibration_check(test_input, test_operations) == expected_return
