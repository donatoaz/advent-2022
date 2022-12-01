import pytest
import os

from day01.calorie_counting import part_1, part_2

@pytest.fixture
def sample_input():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

@pytest.fixture
def my_input():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding="utf8") as f:
        return f.read()

def test_part_1_sample(sample_input):
    assert part_1(sample_input) == 24_000

def test_part_1(my_input):
    assert part_1(my_input) == 71_124

def test_part_2_sample(sample_input):
    assert part_2(sample_input) == 45_000

def test_part_2(my_input):
    assert part_2(my_input) == 204_639
