"""
LeetCode Problem: Remove Duplicates from Sorted Array
Problem Number: 26
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, nums):
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow