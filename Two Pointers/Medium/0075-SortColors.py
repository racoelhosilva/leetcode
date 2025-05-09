"""
LeetCode Problem: Sort Colors
Problem Number: 75
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/sort-colors/
"""

class Solution:
    # Frequency Counting
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def sortColors(self, nums):
        from collections import defaultdict

        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        idx = 0
        for color in range(3):
            freq = freqs[color]
            nums[idx : idx + freq] = [color] * freq
            idx += freq

    # Three Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def sortColors(self, nums):
        r, b = 0, len(nums) - 1
        idx = 0
        while idx <= b:
            if nums[idx] == 0:
                nums[r], nums[idx] = nums[idx], nums[r] 
                r += 1
            elif nums[idx] == 2:
                nums[b], nums[idx] = nums[idx], nums[b]
                b -= 1
                idx -= 1
            idx += 1 

    # Three Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def sortColors(self, nums):
        r = w = b = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                nums[b] = 2
                b += 1
                nums[w] = 1
                w += 1
                nums[r] = 0
                r += 1
            elif nums[idx] == 1:
                nums[b] = 2
                b += 1
                nums[w] = 1
                w += 1
            else:
                nums[w] = 1
                w += 1

    # Three Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def sortColors(self, nums):
        r, w = 0, 0
        for b in range(len(nums)):
            tmp = nums[b]
            nums[b] = 2
            if tmp < 2:
                nums[w] = 1
                w += 1
            if tmp < 1:
                nums[r] = 0
                r += 1
