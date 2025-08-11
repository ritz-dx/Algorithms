import sys
import os
import pytest

# Ensure src is in the path for import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from BinarySearchQuestions import search, search_insert, next_greatest_letter, count_negatives, find_median_sorted_arrays

def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_search_insert():
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4

def test_next_greatest_letter():
    assert next_greatest_letter(["c", "f", "j"], "a") == "c"
    assert next_greatest_letter(["c", "f", "j"], "c") == "f"
    assert next_greatest_letter(["x", "x", "y", "y"], "z") == "x"

def test_count_negatives():
    assert count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert count_negatives([[3, 2], [1, 0]]) == 0

def test_find_median_sorted_arrays():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
