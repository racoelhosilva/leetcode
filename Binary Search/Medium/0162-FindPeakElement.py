"""
LeetCode Problem: Find Peak Element
Problem Number: 162
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/find-peak-element/
"""

class Solution:
    # Binary Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
