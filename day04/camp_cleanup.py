

def parse_input(input: str) -> list[str]:
    return [
        [(int(assignment.split("-")[0]), int(assignment.split("-")[1]))
         for assignment in pair.split(",")]
        for pair in input.strip().split("\n")
    ]


def part_1(input):
    pairs = parse_input(input)

    fully_contained = [
        1 for ((a, b), (c, d)) in pairs
        if a <= c and b >= d or c <= a and d >= b]

    return len(fully_contained)


def part_2(input):
    pairs = parse_input(input)

    overlapping = [
        1 for ((a, b), (c, d)) in pairs
        if a <= c and c <= b or c <= a and a <= d]

    return len(overlapping)
