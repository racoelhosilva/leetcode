"""
LeetCode Problem: Contains Duplicate II
Problem Number: 219
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/contains-duplicate-ii/
"""

class Solution:
    # Hash Map
    # Track the index of the last occurence of element
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsNearbyDuplicate(self, nums, k):
        seen = dict()
        for idx in range(len(nums)):
            if nums[idx] in seen and (idx - seen[nums[idx]]) <= k:
                return True
            seen[nums[idx]] = idx
        return False

    # Sliding Window + Hash Set
    # Keep track of the last k elements
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    def containsNearbyDuplicate(self, nums, k):
        nearby = set()
        for idx in range(len(nums)):            
            if nums[idx] in nearby:
                return True
            nearby.add(nums[idx])
            if idx >= k:
                nearby.remove(nums[idx-k])
        return False
