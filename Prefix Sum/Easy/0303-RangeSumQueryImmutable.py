"""
LeetCode Problem: Range Sum Query Immutable
Problem Number: 303
Difficulty: Easy
Topic: Prefix Sum
Link: https://leetcode.com/problems/range-sum-query-immutable/
"""

# Prefix Sum Array
# Space Complexity: O(n)
class NumArray:
    # Initializing the prefix array
    # Time Complexity: O(n)
    def __init__(self, nums):
        self.prefix_array = [0] * len(nums)
        self.prefix_array[0] = nums[0]
        for idx in range(1, len(nums)):
            self.prefix_array[idx] = nums[idx] + self.prefix_array[idx-1]

    # Querying the sum range
    # Time Complexity: O(1)
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_array[right]
        else:
            return self.prefix_array[right] - self.prefix_array[left - 1]
