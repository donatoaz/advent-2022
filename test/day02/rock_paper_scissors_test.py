import pytest
import os

from day02.rock_paper_scissors import part_1, part_2

@pytest.fixture
def sample_input():
  return """A Y
B X
C Z
"""

@pytest.fixture
def my_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding="utf8") as f:
        return f.read()

def test_part_1_sample_input(sample_input):
  assert part_1(sample_input) == 15

def test_part_1(my_input):
  assert part_1(my_input) == 11449

def test_part_2_sample_input(sample_input):
  assert part_2(sample_input) == 12

def test_part_2(my_input):
  assert part_2(my_input) == 13187