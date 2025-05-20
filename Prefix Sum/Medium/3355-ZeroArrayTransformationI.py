"""
LeetCode Problem: Zero Array Transformation I
Problem Number: 3355
Difficulty: Medium
Topic: Prefix Sum
Link: https://leetcode.com/problems/zero-array-transformation-i/
"""

class Solution:
    # Prefix Sum
    # Time Complexity: O(n + m)
    # Space Complexity: O(n)
    def isZeroArray(self, nums, queries):
        n = len(nums)
        deltas = [0] * (n + 1)
        for l, r in queries:
            deltas[l] += 1
            deltas[r + 1] -= 1
        cur = 0
        for i in range(n):
            cur += deltas[i]
            if cur < nums[i]:
                return False
        return True 
