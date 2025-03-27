"""
LeetCode Problem: Minimum Index of a Valid Split
Problem Number: 2780
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/
"""

class Solution:
    # Boyer-Moore, Count and Check
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minimumIndex(self, nums):
        # Find Majority Element
        candidate = nums[0]
        chance = 0
        for num in nums:
            if chance == 0:
                candidate = num
            if candidate == num:
                chance += 1
            else:
                chance -= 1

        # Count Occurrences
        total_count = 0
        for num in nums:
            if num == candidate:
                total_count += 1

        # Check for Valid Splits
        n = len(nums)
        count = 0
        for idx in range(n):
            if nums[idx] == candidate:
                count += 1
            remaining_count = total_count - count
            if count * 2 > idx + 1 and remaining_count * 2 >= n - idx - 1:
                return idx
        
        return -1
