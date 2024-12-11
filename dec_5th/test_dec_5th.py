from dec_5th import (
    get_correct_update_count,
    check_update,
    rule_test,
    reorder_incorrect_updates,
    reorder_update,
)


class TestGetCorrectUpdateCount:
    def test_func_returns_correct_value_for_test_input(self):
        filepath = "dec_5th/test_input_1.txt"
        expected_return = 143
        assert get_correct_update_count(filepath) == expected_return


class TestReorderIncorrectpdates:
    def test_func_returns_correct_value_for_test_data(self):
        filepath = "dec_5th/test_input_1.txt"
        expected_return = 123
        assert reorder_incorrect_updates(filepath) == expected_return


class TestCheckUpdates:
    def test_check_updates_accepts_update_that_passes_one_rule(self):
        update = [1, 2, 3]
        rules = [[1, 2]]
        expected_return = 2
        assert check_update(update, rules) == expected_return

    def test_check_updates_passes_an_update_that_doesnt_interact_with_the_rule(self):
        update = [1, 2, 3]
        rules = [[4, 5]]
        expected_return = 2
        assert check_update(update, rules) == expected_return

    def test_check_updates_returns_0_when_update_fails_a_rule(self):
        update = [1, 2, 3]
        rules = [[2, 1]]
        expected_return = 0
        assert check_update(update, rules) == expected_return

    def test_check_updates_returns_correct_value_when_update_passes_multiple_tests(
        self,
    ):
        update = [1, 2, 3]
        rules = [[1, 2], [2, 3]]
        expected_return = 2
        assert check_update(update, rules) == expected_return

    def test_check_updates_returns_0_when_update_fails_one_rule_of_several(self):
        update = [1, 2, 3]
        rules = [[1, 2], [3, 2]]
        expected_return = 0
        assert check_update(update, rules) == expected_return


class TestRuleTest:
    def test_func_returns_true_when_update_passes_rule(self):
        update = [1, 2, 3]
        rule = [1, 2]
        expected_return = True
        assert rule_test(update, rule) == expected_return

    def test_func_returns_false_when_update_fails_rule(self):
        update = [1, 2, 3]
        rule = [2, 1]
        expected_return = False
        assert rule_test(update, rule) == expected_return

    def test_func_return_true_when_update_has_only_first_num_in_the_rule(self):
        update = [1, 2, 3]
        rule = [1, 4]
        expected_return = True
        assert rule_test(update, rule) == expected_return

    def test_func_return_true_when_update_has_only_second_num_in_the_rule(self):
        update = [1, 2, 3]
        rule = [4, 1]
        expected_return = True
        assert rule_test(update, rule) == expected_return

    def test_func_return_true_when_update_has_no_nums_in_the_rule(self):
        update = [1, 2, 3]
        rule = [4, 5]
        expected_return = True
        assert rule_test(update, rule) == expected_return


# class TestReorderUpdate:
#     def test_reorder_update_can_reorder_an_update_to_match_one_rule(self):
#         update = [1,2,3,4,5]
#         rules = [[4,3]]
#         expected_return = 4
#         assert reorder_update(update, rules) == expected_return

#     def test_func_can_apply_multiple_rules(self):
#         update = [1,2,3,4,5]
#         rules = [[5,4],[4,3],[3,2],[2,1]]
#         expected_return = 3
#         assert reorder_update(update, rules) == expected_return

# class TestApplyRule:
#     def test_func_can_apply_a_rule_to_a_short_update(self):
#         update = [2,1]
#         rule = [1,2]
#         expected_return = [1,2]
#         assert apply_rule(update, rule) == expected_return

#     def test_func_can_apply_a_rule_to_a_longer_update(self):
#         update = [5,4,3,2,1]
#         rule = [1,2]
#         expected_return = [1,2,5,4,3]
#         assert apply_rule(update, rule) == expected_return


class TestReorderUpdate:
    def test_func_can_apply_a_rule_to_a_short_update(self):
        update = [2, 1]
        rules = [[1, 2]]
        expected_return = [1, 2]
        assert reorder_update(update, rules) == expected_return

    def test_func_can_apply_a_s_to_a_longer_update(self):
        update = [5, 4, 3, 2, 1]
        rules = [[1, 2]]
        expected_return = [5, 4, 3, 1, 2]
        assert reorder_update(update, rules) == expected_return

    def test_func_can_apply_two_unrelated_rules_to_update(self):
        update = [5, 4, 3, 2, 1]
        rules = [[1, 2], [3, 4]]
        expected_return = [5, 3, 4, 1, 2]
        assert reorder_update(update, rules) == expected_return

    def test_func_can_apply_two_related_rules_to_update(self):
        update = [5, 4, 3, 2, 1]
        rules = [[1, 2], [1, 4]]
        expected_return = [5, 1, 4, 3, 2]
        assert reorder_update(update, rules) == expected_return

    def test_func_works_on_complex_example(self):
        update = [75, 97, 47, 61, 53]
        rules = [
            [47, 53],
            [97, 13],
            [97, 61],
            [97, 47],
            [75, 29],
            [61, 13],
            [75, 53],
            [29, 13],
            [97, 29],
            [53, 29],
            [61, 53],
            [97, 53],
            [61, 29],
            [47, 13],
            [75, 47],
            [97, 75],
            [47, 61],
            [75, 61],
            [47, 29],
            [75, 13],
            [53, 13],
        ]
        expected_return = [97, 75, 47, 61, 53]
        assert reorder_update(update, rules) == expected_return
