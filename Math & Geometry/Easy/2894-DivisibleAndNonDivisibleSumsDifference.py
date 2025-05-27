"""
LeetCode Problem: Divisible and Non Divisible Sums Difference
Problem Number: 2894
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
"""

class Solution:
    # Mathematics: Arithmetic Progression
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def differenceOfSums(self, n, m):
        # Number of elements in [1,n] divisible by m
        s = n // m
        # Sum of progression a(n) = a(1) + (n - 1) * m {multiples of m in [1,n]}
        t = s * (m + m * s) / 2
        # Sum of progressin a(n) = a(1) + n - 1 {numbers in [1,n]}
        u = n * (n + 1) / 2
        # Result is difference between u and 2 * t
        return u - 2 * t
