


def part_1(input: str):
    elven_meals = [map(int, calories.split("\n")) for calories in input.strip().split("\n\n")]

    total_cals_per_elf = [sum(calories) for calories in elven_meals]

    return max(total_cals_per_elf) 
