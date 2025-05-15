# --- Day 5: Print Queue ---

# Satisfied with their search on Ceres, the squadron of scholars suggests subsequently
# scanning the stationery stacks of sub-basement 17.

# The North Pole printing department is busier than ever this close to Christmas,
# and while The Historians continue their search of this historically significant
# facility, an Elf operating a very familiar printer beckons you over.

# The Elf must recognize you, because they waste no time explaining that the new sleigh
# launch safety manual updates won't print correctly. Failure to update the safety
# manuals would be dire indeed, so you offer your services.

# Safety protocols clearly indicate that new pages for the safety manuals must be
# printed in a very specific order. The notation X|Y means that if both page number X
# and page number Y are to be produced as part of an update, page number X must be
# printed at some point before page number Y.

# The Elf has for you both the page ordering rules and the pages to produce in each
# update (your puzzle input), but can't figure out whether each update has the pages
# in the right order.

# For example:

# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47

# The first section specifies the page ordering rules, one per line. The first rule, 47|53,
# means that if an update includes both page number 47 and page number 53, then page number 47
# must be printed at some point before page number 53. (47 doesn't necessarily need to be
# immediately before 53; other pages are allowed to be between them.)

# The second section specifies the page numbers of each update. Because most safety manuals
# are different, the pages needed in the updates are different too. The first update,
# 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

# To get the printers going as soon as possible, start by identifying which updates are
# already in the right order.

# In the above example, the first update (75,47,61,53,29) is in the right order:

#   75 is correctly first because there are rules that put each other page after it:
#       75|47, 75|61, 75|53, and 75|29.
#   47 is correctly second because 75 must be before it (75|47) and every other page must
#       be after it according to 47|61, 47|53, and 47|29.
#   61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61)
#       and 53 and 29 are after it (61|53 and 61|29).
#   53 is correctly fourth because it is before page number 29 (53|29).
#
#   29 is the only page left and so is correctly last.

# Because the first update does not include some page numbers, the ordering rules involving
# those missing page numbers are ignored.

# The second and third updates are also in the correct order according to the rules.
# Like the first update, they also do not include every page number, and so only some of
# the ordering rules apply - within each update, the ordering rules that involve missing page
# numbers are not used.

# The fourth update, 75,97,47,61,53, is not in the correct order: it would print 75 before 97,
# which violates the rule 97|75.

# The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.

# The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

# For some reason, the Elves also need to know the middle page number of each update being printed.
# Because you are currently only printing the correctly-ordered updates, you will need to find
# the middle page number of each correctly-ordered update. In the above example, the correctly-ordered
# updates are:

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13

# These have middle page numbers of 61, 53, and 29 respectively.
# Adding these page numbers together gives 143.

# Of course, you'll need to be careful: the actual list of page ordering rules is bigger
# and more complicated than the above example.

# Determine which updates are already in the correct order.
# What do you get if you add up the middle page number from those correctly-ordered updates?

# --- Part Two ---

# While the Elves get to work printing the correctly-ordered updates, you have a little
# time to fix the rest of them.

# For each of the incorrectly-ordered updates, use the page ordering rules to put the page
# numbers in the right order. For the above example, here are the three incorrectly-ordered
# updates and their correct orderings:

#     75,97,47,61,53 becomes 97,75,47,61,53.
#     61,13,29 becomes 61,29,13.
#     97,13,75,29,47 becomes 97,75,47,29,13.

# After taking only the incorrectly-ordered updates and ordering them correctly, their
# middle page numbers are 47, 29, and 47. Adding these together produces 123.

# Find the updates which are not in the correct order. What do you get if you add up
# the middle page numbers after correctly ordering just those updates?


from pprint import pprint
from math import floor


def get_correct_update_count(filepath):
    """
    this function takes the input file and processes it by:
        - splitting it into rules and updates
        - splitting those rules and updates into their component numbers
        - calling int() on those numbers
    it then reutrns the sum of the middle values of the passing updates,
    as determined by check_update()
    """
    with open(filepath) as file:
        rule_data, update_data = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rule_data.split("\n")]
    updates = [update.split(",") for update in update_data.split("\n")]

    check_update = lambda update, rules: all(
        [rule_test(update, rule) for rule in rules]
    ) * int(update[floor(len(update) / 2)])

    return sum(check_update(update, rules) for update in updates if update != [""])


# def check_update(update, rules):
#     """
#     this function compares a single update to all rules by calling rule_test()
#     it returns 0 if any rule test fails, otherwise it returns the middle value of the update
#     to do this it returns the middle value multiplied by all() on a list comprehension of the
#     rules tests. if any fail then the all() is false and is treated as 0 by the multiplication
#     """

#     return all([rule_test(update, rule) for rule in rules]) * int(
#         update[floor(len(update) / 2)]
#     )


def rule_test(update, rule):
    """
    this function tests if an update passes a rule. first it checks if the rule applies to the update
    ie that both nums in the rule are in the update and returns true if the rule does not apply.
    then it iterates through the updates, and returns true if it encounters the first num in the rule
    first and false if it encounters the second num in the rule first
    """
    if rule[0] in update and rule[1] in update:
        for num in update:
            if num == rule[0]:
                return True
            elif num == rule[1]:
                return False
    return True


def reorder_incorrect_updates(filepath):
    """
    this function fetches the file data as in get_correct_update_count()
    then it calls reorder_update on the updates that fail the rules,
    and returns the sum of the middle values as teh puzzle solution"""
    with open(filepath) as file:
        rule_data, update_data = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rule_data.split("\n")]
    updates = [update.split(",") for update in update_data.split("\n")]

    middle_nums = [
        int(update[floor(len(update) / 2)])
        for update in [
            reorder_update(update, rules)
            for update in [
                update
                for update in updates
                if not all(rule_test(update, rule) for rule in rules)
            ]
        ]
    ]

    return sum(middle_nums)


def reorder_update(update, rules):
    """this function takes an update and checks it against each rule
    when it finds a rule that is broken, it first iterates through the update to
    find the number that should be first according to the rule and removes it.
    then it iterates through the update to find the number that should come second
    and inserts the first number directly before it.

    finally checks the update aginst all the rules, and if the update fails any rule
    the function applies itself recursively
    """
    for rule in rules:
        if rule[0] in update and rule[1] in update and not rule_test(update, rule):
            for i in range(len(update)):
                if update[i] == rule[0]:
                    update = update[:i] + update[i + 1 :]
                    break
            for i in range(len(update)):
                if update[i] == rule[1]:
                    update = update[:i] + rule + update[i + 1 :]
                    break

    if all([rule_test(update, rule) for rule in rules]):
        return update
    else:
        return reorder_update(update, rules)


if __name__ == "__main__":
    pprint(
        f"GET CORRECT UPDATE COUNT: {get_correct_update_count('dec_5th/input_1.txt')}"
    )
    pprint(
        f"REORDER INCORRECT UPDATES: {reorder_incorrect_updates('dec_5th/input_1.txt')}"
    )
