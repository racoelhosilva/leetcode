"""
LeetCode Problem: Single Number
Problem Number: 136
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/single-number/
"""

class Solution:
    # Brute Force Search
    # Time Complexity: O(n^2) -> Time Limit Exceeded
    # Space Complexity: O(1)
    def singleNumber(self, nums):
        for i in range(len(nums)):
            single = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    single = False
                    break
            if single:
                return nums[i]
            
    # Hash Set
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def singleNumber(self, nums):
        freq = set()
        for num in nums:
            if num in freq:
                freq.remove(num)
            else:
                freq.add(num)
        return freq.pop()
    
    # Sorting and Searching
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def singleNumber(self, nums):
        nums = sorted(nums)
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx+1]:
                idx += 2
            else:
                return nums[idx]
        return nums[idx]

    # XOR Operations
    # Single the xor of two equal numbers is 0
    # Performing XOR on the entire list will leave the single
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber(self, nums):
        single = 0
        for num in nums:
            single ^= num
        return single
