"""
LeetCode Problem: Divide Array Into Equal Pairs
Problem Number: 2206
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/divide-array-into-equal-pairs/
"""

class Solution:
    # Sorting
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def divideArray(self, nums):
        if len(nums) % 2 == 1:
            return False
        
        nums = sorted(nums)
        for idx in range(0, len(nums), 2):
            if nums[idx] != nums[idx + 1]:
                return False
        return True

    # Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def divideArray(self, nums):
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        for _num, freq in freqs.items():
            if freq % 2 == 1:
                return False 
        return True
    
    # Hash Set
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def divideArray(self, nums):
        unmatched = set()
        for num in nums:
            if num in unmatched:
                unmatched.remove(num)
            else:
                unmatched.add(num)
        return len(unmatched) == 0
