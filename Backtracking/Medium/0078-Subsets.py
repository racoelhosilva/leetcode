"""
LeetCode Problem: Subsets
Problem Number: 78
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/subsets/
"""

class Solution:
    # Backtracking
    # Recursively accumulate the sets including and excluding the given element
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n * 2^n)
    def subsets(self, nums):
        res = []
        def backtracking(n, subset):
            res.append(subset[:])
            for idx in range(n, len(nums)):
                subset.append(nums[idx])
                backtracking(idx + 1, subset)
                subset.pop()
        backtracking(0, [])
        return res

    # Iteration
    # For each number and each existing subset, create a new subset
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n * 2^n)
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res.extend([subset + [num] for subset in res])
        return res

    # Bit mask
    # Use numbers as bitmasks for the elements in the original list
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n * 2^n)
    def subsets(self, nums):
        res = []
        for mask in range(1 << len(nums)):
            subset = []
            idx = 0
            while mask > 0:
                if mask & 1:
                    subset.append(nums[idx])
                idx += 1
                mask >>= 1
            res.append(subset)
        return res
