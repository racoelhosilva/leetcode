"""
LeetCode Problem: Maximum Count of Positive Integer and Negative Integer
Problem Number: 2529
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
"""

class Solution:
    # Linear Search
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maximumCount(self, nums):
        pos = neg = 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
        return max(neg, pos)

    # Binary Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def maximumCount(self, nums):
        n = len(nums) - 1
        def lower_bound():
            l, r = 0, n
            index = len(nums)
            while l <= r:
                m = (l + r) // 2
                if nums[m] < 0:
                    l = m + 1
                else:
                    r = m - 1
                    index = m
            return index

        def upper_bound():
            l, r = 0, n
            index = len(nums)
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= 0:
                    l = m + 1
                else:
                    r = m - 1
                    index = m
            return index

        neg = lower_bound()
        pos = len(nums) - upper_bound()
        return max(neg, pos)
