from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Binary search for target in sorted list nums.
    Returns index if found, else -1.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def search_insert(nums: List[int], target: int) -> int:
    """
    Returns the index if target is found in nums, else the index where it should be inserted.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Returns the smallest character in letters that is lexicographically greater than target.
    If not found, returns the first character in letters.
    """
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]

def count_negatives(grid: List[List[int]]) -> int:
    """
    Counts the number of negative numbers in a sorted matrix.
    """
    count = 0
    for row in grid:
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        count += len(row) - left
    return count

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Returns the median of two sorted arrays.
    """
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return float(merged[mid])
