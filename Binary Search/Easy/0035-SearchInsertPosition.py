"""
LeetCode Problem: Search Insert Position
Problem Number: 35
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/search-insert-position/
"""

class Solution:
    # Binary Search
    # Keeping res lower bounded
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums, target):
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
                res = mid
            else:
                return mid
        return res

    # Binary Search
    # Forcing l pointer to pass the r pointer
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
    
    # Binary Search
    # Lower bound 
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2  
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l
    