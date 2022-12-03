

def parse_input(input: str) -> list[tuple[str, str]]:
  return [
    (line[:len(line)//2], line[len(line)//2:]) 
    for line in input.strip().split("\n")
  ]

def priority(char: str) -> int:
  return ord(char) - (96 if char.islower() else 38)


def part_1(input):
  rucksacks = parse_input(input)

  repeats = [set([*left]).intersection([*right]).pop() for (left, right) in rucksacks]

  priorities = [
    priority(item) for item in repeats
  ]

  return sum(priorities)
  

def part_2(input):
  rucksacks = parse_input(input)

  groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]

  # TODO: refactor to map-reduce or list comprehension
  priorities = []

  for group in groups:
    items = [left + right for left, right in group]
    badge = set([*items[0]]).intersection([*items[1]]).intersection([*items[2]]).pop()

    priorities.append(priority(badge))

  return sum(priorities)