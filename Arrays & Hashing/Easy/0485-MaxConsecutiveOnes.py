"""
LeetCode Problem: Max Consecutive Ones
Problem Number: 485
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/max-consecutive-ones/
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res
