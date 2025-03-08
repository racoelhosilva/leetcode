"""
LeetCode Problem: Search in Rotated Sorted Array
Problem Number: 33
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    # Binary Search
    # To prune the search space, first verify which half is sorted
    # Note: since the search is left-biased, the left condition contains ==
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
