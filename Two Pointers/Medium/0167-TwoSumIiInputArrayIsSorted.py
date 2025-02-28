"""
LeetCode Problem: Two Sum II Input Array Is Sorted
Problem Number: 167
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []
    
    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, numbers, target):
        viewed = dict()
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in viewed:
                return [viewed[diff]+1, i+1]
            viewed[numbers[i]] = i
        return []

    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l+1, r+1]
        return []