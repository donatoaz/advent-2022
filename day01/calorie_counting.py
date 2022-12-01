


def part_1(input: str) -> int:
    elven_meals = [map(int, calories.split("\n")) for calories in input.strip().split("\n\n")]

    total_cals_per_elf = [sum(calories) for calories in elven_meals]

    return max(total_cals_per_elf) 

def part_2(input: str) -> int:
    elven_meals = [map(int, calories.split("\n")) for calories in input.strip().split("\n\n")]

    total_cals_per_elf = [sum(calories) for calories in elven_meals]

    sorted_total_cals_per_elf = sorted(total_cals_per_elf, reverse=True)

    return sum(sorted_total_cals_per_elf[:3])