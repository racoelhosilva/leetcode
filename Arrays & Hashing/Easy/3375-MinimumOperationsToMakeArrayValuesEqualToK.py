"""
LeetCode Problem: Minimum Operations to Make Array Values Equal to K
Problem Number: 3375
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
"""

class Solution:
    # Hash Set
    # What this problem wants to do is given an array of numbers, we want to transform all values into k
    # To transform numbers, we can perform the following operation
    # Select a number i such that all numbers that are greater than i are equal
    # This means that i is the second largest number in the array (there may be multiple instances of the largest)
    # With this number i, we can now change all values > i into this i value, making them the largest elements (with repetitions)
    # We want to know how many times we can perform this operation to make all values equal to k
    #
    # Observations: 
    # - this operation can only make the numbers smaller, so if there is an element < k, it is impossible
    # - since the operation transforms all numbers in the array, we only need to worry about the distinct numbers greater than k
    #
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minOperations(self, nums, k):
        seen = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                seen.add(num)
        return len(seen)
