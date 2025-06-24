"""
LeetCode Problem: Find All K Distant Indices in an Array
Problem Number: 2200
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
"""

class Solution:
    # Single Traversal
    # Time Complexity: O(n * k)
    # Space Complexity: O(n)
    def findKDistantIndices(self, nums, key, k):
        res = []
        r = 0
        for idx in range(len(nums)):
            if nums[idx] == key:
                l = max(r, idx - k)
                r = min(len(nums) - 1, idx + k) + 1
                for cur in range(l, r):
                    res.append(nums[cur])
        return res
