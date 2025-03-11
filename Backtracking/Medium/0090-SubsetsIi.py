"""
LeetCode Problem: Subsets II
Problem Number: 90
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/subsets-ii/
"""

class Solution:
    # Bactracking
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(cur, subset):
            res.append(subset[:])
            for idx in range(cur, len(nums)):
                if idx > cur and nums[idx] == nums[idx-1]:
                    continue
                subset.append(nums[idx])
                backtrack(idx + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res