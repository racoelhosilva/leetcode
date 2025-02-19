"""
LeetCode Problem: Two Sum
Problem Number: 1
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    # Brute Force Approach
    # For each number, we search for the complement needed to equal the target
    # in the rest of the number list
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # Two-Pass Hash Table
    # Store each number and its index in a hash map
    # For each number, check if there is another valid complement in the list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums, target):
        viewed = dict()
        for i in range(len(nums)):
            viewed[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in viewed and viewed[diff] != i:
                return [i, viewed[diff]]
        return []

    # One-Pass Hash Table
    # For each number, check if a valid complement was already seen
    # Otherwise, add the number and its index to the hash map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums, target):
        viewed = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in viewed:
                return [i, viewed[diff]]
            viewed[nums[i]] = i
        return []
