"""
LeetCode Problem: Sqrtx
Problem Number: 69
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/sqrtx/
"""

class Solution:
    # Binary Search (Bounded res)
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
    
    # Binary Search
    # We keep a bound on the l pointer to make sure it never overshoots the target
    # The search is right-biased and we don't need to run when l == r
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def mySqrt(self, x):
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left
    
    # Newton's Method
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def mySqrt(self, x):
        res = x
        while res * res > x:
            res = (res + x // res) // 2
        return res
