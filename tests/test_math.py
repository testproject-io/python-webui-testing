"""
This module contains the first test case of the tutorial.
It's a simple arithmetic check.
Its purpose is to show how pytest works.
"""

import pytest


def test_addition():
  assert 1 + 1 == 2


def test_subtraction():
  diff = 1 - 1
  assert diff == 0
  # To see a failure:
  # assert diff == 1


@pytest.mark.parametrize(
  "a,b,expected",
  [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
def test_multiplication(a, b, expected):
  assert a * b == expected


def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    1 / 0
