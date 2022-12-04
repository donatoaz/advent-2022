import pytest
import os

from day04.camp_cleanup import part_1, part_2


@pytest.fixture
def sample_input():
  return """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.fixture
def my_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding="utf8") as f:
        return f.read()


def test_part_1_sample_input(sample_input):
  assert part_1(sample_input) == 2


def test_part_1(my_input):
  assert part_1(my_input) == 462


def test_part_2_sample_input(sample_input):
  assert part_2(sample_input) == 4


def test_part_2(my_input):
  assert part_2(my_input) == 835
