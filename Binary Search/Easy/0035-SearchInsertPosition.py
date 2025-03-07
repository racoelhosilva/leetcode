"""
LeetCode Problem: Search Insert Position
Problem Number: 35
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/search-insert-position/
"""

class Solution:
    # Binary Search (Bounded res)
    # When the value at mid is larger than target, its index is a candidate
    # We keep track of these candidates in case the value does not exist
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
                res = mid
                r = mid - 1
            else:
                return mid
        return res

    # Binary Search
    # This is the same idea of the previous approach
    # Instead of using another variable, we can use the l pointer
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
    # We keep a bound on the r pointer to make sure it never overshoots the target
    # The search is left-biased, left is incremented and we don't need to run when l == r
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2  
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l
    