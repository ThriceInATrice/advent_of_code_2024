from dec_9th import sort_files


class TestSortFiles:
    def test_func_on_simple_case(self):
        test_input = "dec_9th/test_input_1.txt"
        expected_return = 60
        assert sort_files(test_input) == expected_return

    def test_func_on_example_case(self):
        test_input = "dec_9th/test_input_2.txt"
        expected_return = 1928
        assert sort_files(test_input) == expected_return
