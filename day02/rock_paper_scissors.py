

def parse_input(input: str) -> list[str]:
  return input.strip().split("\n")

win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3

opponent_rock = "A"
opponent_paper = "B"
opponent_scissors = "C"

my_rock = "X"
my_paper = "Y"
my_scissors = "Z"

should_lose = "X"
should_draw = "Y"
should_win = "Z"

scores_map = dict([
  (f'{opponent_rock} {my_rock}', rock + draw),
  (f'{opponent_rock} {my_paper}', paper + win),
  (f'{opponent_rock} {my_scissors}', scissors + loss),

  (f'{opponent_paper} {my_rock}', rock + loss),
  (f'{opponent_paper} {my_paper}', paper + draw),
  (f'{opponent_paper} {my_scissors}', scissors + win),

  (f'{opponent_scissors} {my_rock}', rock + win),
  (f'{opponent_scissors} {my_paper}', paper + loss),
  (f'{opponent_scissors} {my_scissors}', scissors + draw),
])

def part_1(input: str):
  plays = parse_input(input)

  scores = [scores_map[play] for play in plays]

  return sum(scores)

new_scores_map = dict([
  (f'{opponent_rock} {should_win}', paper + win),
  (f'{opponent_rock} {should_draw}', rock + draw),
  (f'{opponent_rock} {should_lose}', scissors + loss),

  (f'{opponent_paper} {should_win}', scissors + win),
  (f'{opponent_paper} {should_draw}', paper + draw),
  (f'{opponent_paper} {should_lose}', rock + loss),

  (f'{opponent_scissors} {should_win}', rock + win),
  (f'{opponent_scissors} {should_draw}', scissors + draw),
  (f'{opponent_scissors} {should_lose}', paper + loss),
])

def part_2(input):
  plays = parse_input(input)
  
  scores = [new_scores_map[play] for play in plays]

  return sum(scores)