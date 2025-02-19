"""
LeetCode Problem: Contains Duplicate
Problem Number: 217
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    # Hash Set
    # Keep track of which elements have already appeared with a set
    # In case an element is repeated, duplicate is found
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicate(self, nums):
        elems = set()
        for num in nums:
            if num in elems:
                return True
            elems.add(num)
        return False
    
    # Python Shorthands
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
