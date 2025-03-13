"""
LeetCode Problem: Kids With the Greatest Number of Candies
Problem Number: 1431
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

class Solution:
    # Two Pass (Maximum + Answer)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def kidsWithCandies(self, candies, extraCandies):
        target = -1
        for numCandies in candies:
            if numCandies > target:
                target = numCandies

        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= target:
                res[i] = True
        return res
