import argparse
import pathlib

parser = argparse.ArgumentParser(
    prog="aoc-bootstrapper",
)

parser.add_argument('dirname')
parser.add_argument('title')
args = parser.parse_args()

# create src folder
pathlib.Path(args.dirname).mkdir(parents=True, exist_ok=True)

# create src file
with open(args.dirname + '/__init__.py', 'w', encoding='utf8') as f:
  f.write("")

with open(args.dirname + '/' + args.title + '.py', 'w', encoding='utf8') as f:
  f.write("""

def parse_input(input: str) -> Any:
  pass

def part_1(input):
  pass

def part_2(input):
  pass
""")

# create test folder
pathlib.Path('test/' + args.dirname).mkdir(parents=True, exist_ok=True)

# create input file
with open('test/' + args.dirname + '/input.txt', 'w', encoding='utf8') as f:
  f.write("")

# create test files
with open('test/' + args.dirname + '/__init__.py', 'w', encoding='utf8') as f:
  f.write("")

with open('test/' + args.dirname + '/' + args.title + '_test.py', 'w', encoding='utf8') as f:
  f.write("""import pytest
import os

from %s.%s import part_1, part_2

@pytest.fixture
def sample_input():
  return\"\"\"
REPLACE HERE
\"\"\"

@pytest.fixture
def my_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding="utf8") as f:
        return f.read()

def test_part_1_sample_input(sample_input):
  assert part_1(sample_input) == 0

def test_part_1(my_input):
  assert part_1(my_input) == 0

def test_part_2_sample_input(sample_input):
  assert part_2(sample_input) == 0

def test_part_2(my_input):
  assert part_2(my_input) == 0

""" % (args.dirname, args.title))
