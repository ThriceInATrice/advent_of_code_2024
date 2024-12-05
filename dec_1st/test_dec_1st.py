from dec_1st import get_sum_of_differenes, get_similarity_sum


class TestGetSumOfDifferences:
    def test_func_returns_correct_sum_for_test_input(self):
        test_filepath = "dec_1st/test_input_1.txt"
        assert get_sum_of_differenes(test_filepath) == 11


class TestGetSimilaritySum:
    def test_func_returns_correct_sum_for_test_input(self):
        test_filepath = "dec_1st/test_input_1.txt"
        assert get_similarity_sum(test_filepath) == 31
