from dec_2nd import get_safety_count, step_check


class TestGetSafetyCount:
    def test_if_func_returns_correct_value_for_test_data(self):
        expected_value = 2
        test_filepath = "dec_2nd/test_input_1.txt"
        assert get_safety_count(test_filepath, 0) == expected_value


class TestStepCheckWithNoDamper:
    def test_step_check_on_gradual_ascending(self):
        test_line = [1, 2, 3]
        expected_return = True
        assert step_check(test_line, 0) == expected_return

    def test_step_check_with_gradual_ascending(self):
        test_line = [3, 2, 1]
        expected_return = True
        assert step_check(test_line, 0) == expected_return

    def test_step_check_with_gradual_uneven(self):
        test_line = [1, 3, 2]
        expected_return = False
        assert step_check(test_line, 0) == expected_return

    def test_if_step_check_catches_0_gradient(self):
        test_line = [1, 2, 2]
        expected_return = False
        assert step_check(test_line, 0) == expected_return

    def test_step_check_catches_sharp_gradient(self):
        test_line = [1, 5, 10]
        expected_return = False
        assert step_check(test_line, 0) == expected_return

        test_line_2 = [20, 15, 10]
        expected_return_2 = False
        assert step_check(test_line_2, 0) == expected_return_2

class TestStepCheckWithDamper:
    def test_step_check_accepts_lines_with_no_issues_while_damper_is_on(self):
        test_line = [1,2,4]
        expected_return = True
        assert step_check(test_line, 1) == expected_return
    
    def test_step_check_accepts_asceinding_with_one_descending(self):
        test_line = [1, 2, 1, 5]
        expected_return = True
        assert step_check(test_line, 1) == expected_return
    
    def test_step_check_rejects_ascending_line_with_two_descending(self):
        test_line = [1, 2, 3, 2, 1, 4]
        expected_return = False
        assert step_check(test_line, 1) == expected_return

    def test_step_check_rejects_ascending_line_with_one_naieve_descent(self):
        """this test would be failed by a function that naievely checks for diferences between elements
        if that function saw 6 -> 1 as the only point of issue"""
        
        test_line = [5, 6, 1, 2, 3]
        expected_return = False
        assert step_check(test_line, 1) == expected_return