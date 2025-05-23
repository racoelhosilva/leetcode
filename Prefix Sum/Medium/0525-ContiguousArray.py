"""
LeetCode Problem: Contiguous Array
Problem Number: 525
Difficulty: Medium
Topic: Prefix Sum
Link: https://leetcode.com/problems/contiguous-array/
"""

class Solution:
    # Prefix Sum
    # At each step, increment the current streak by 1 if num == 1 or decrement by 1 if num == 0
    # Tracking the sum in a plot over n, we see that it increases or decreases
    # A sequence with an equal count of 0 and 1 appears when the streak goes over a number previously visited
    # So we can keep track of the indices of first appearance of the streak and return the maximum difference
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findMaxLength(self, nums):
        first = {0:-1}
        res = 0
        cur = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                cur -= 1
            else:
                cur += 1
            
            if cur in first:
                res = max(res, idx - first[cur])
            else:
                first[cur] = idx

        return res
