"""
LeetCode Problem: Find Minimum in Rotated Sorted Array
Problem Number: 153
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    # Binary Search
    # If the array was initially sorted, we need the index of the previous first element
    # On a rotated sorted array, this corresponds to the first element smaller than the previous
    # We can perform a left-biased search while not overshooting the r pointer
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    # Binary Search
    # If the array was initially sorted, we need the index of the previous first element
    # On a rotated sorted array, this corresponds to the first element smaller than the previous
    # We can perform a left-biased search while not overshooting the r pointer
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
