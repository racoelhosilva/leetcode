"""
LeetCode Problem: Sqrtx
Problem Number: 69
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/sqrtx/
"""

class Solution:
    # Binary Search
    # Perform binary search on the interval, considering left value as candidate
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def mySqrt(self, x):
        left, right = 0, x
        res = 0
        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                res = mid
            else:
                return mid
        return res
    
    # Newton's Method
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def mySqrt(self, x):
        res = x
        while res * res > x:
            res = (res + x // res) // 2
        return res
