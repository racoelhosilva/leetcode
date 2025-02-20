"""
LeetCode Problem: Move Zeroes
Problem Number: 283
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/move-zeroes/
"""

class Solution:
    # Two Pointer Approach (Two pass)
    # Fast pointer: goes through the list skipping zeroes
    # Slow pointer: position of next non-zero element
    # After fast pointer reaches end, slow pointer fills rest with zeroes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        return nums
    
    # Two Pointer Approach (One pass)
    # Slight optimization can be made by swapping the two values
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums
