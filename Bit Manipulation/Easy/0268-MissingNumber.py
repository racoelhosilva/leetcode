"""
LeetCode Problem: Missing Number
Problem Number: 268
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/missing-number/
"""

class Solution:
    # Sorting
    # Sort the algorithm and check for the first unmatched index
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def missingNumber(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    
    # Sum of Sequence
    # Using Gauss sumation, we can find the missing number
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber(self, nums):
        target = (len(nums) * (len(nums) + 1)) / 2
        for num in nums:
            target -= num
        return target
    
    # Bit Manipulation
    # Following the unmatched index idea, perform XOR operations
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res