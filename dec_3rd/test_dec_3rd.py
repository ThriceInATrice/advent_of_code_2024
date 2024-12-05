from dec_3rd import do_mul, get_muls, get_do_dont_muls


class TestGet_Muls:
    def test_get_muls_gives_correct_value_for_test_input(self):
        expected_value = 161
        test_filepath = "dec_3rd/test_input_1.txt"
        assert get_muls(test_filepath) == expected_value


class TestDoDontMuls:
    def test_if_func_returns_correct_value_test_input_2(self):
        expected_value = 48
        test_filepath = "dec_3rd/test_input_2.txt"
        assert get_do_dont_muls(test_filepath) == expected_value


class TestDoMul:
    def test_do_mul_returns_correct_values(self):
        assert do_mul("mul(2,2)") == 4
        assert do_mul("mul(3,6)") == 18
        assert do_mul("mul(200,40)") == 8000
