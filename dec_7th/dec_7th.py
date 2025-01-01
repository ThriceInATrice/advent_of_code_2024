def get_calibration_sum(filepath, operations):
    with open(filepath) as file:
        calibrations = [
            (int(line_data[0]), [int(num) for num in line_data[1].split(" ")])
            for line_data in [line.split(": ") for line in file]
        ]

    possible_calibrations = [
        calibration_check(calibration, operations) for calibration in calibrations
    ]

    return sum(possible_calibrations)


def calibration_check(calibration, operations):
    target, nums = calibration
    if len(nums) > 1:
        if "mult" in operations:
            product = nums[0] * nums[1]
            if product <= target:
                next_step = calibration_check(
                    [target, [product] + nums[2:]], operations
                )
                if next_step:
                    return next_step

        if "add" in operations:
            sum = nums[0] + nums[1]
            if sum <= target:
                next_step = calibration_check([target, [sum] + nums[2:]], operations)
                if next_step:
                    return next_step

        if "concat" in operations:
            concat = int(str(nums[0]) + str(nums[1]))
            if concat <= target:
                next_step = calibration_check([target, [concat] + nums[2:]], operations)
                if next_step:
                    return next_step

    return target if nums[0] == target else False


if __name__ == "__main__":
    print(
        f"""PART 1: {
            get_calibration_sum('dec_7th/input_1.txt', 
                                ['mult', 'add']
            )
        }"""
    )

    print(
        f"""PART 2: {
            get_calibration_sum('dec_7th/input_1.txt', 
                                ['mult', 'add', 'concat']
            )
        }"""
    )
