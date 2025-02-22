"""
LeetCode Problem: Remove Element
Problem Number: 27
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/remove-element/
"""

class Solution:
    # Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow 
