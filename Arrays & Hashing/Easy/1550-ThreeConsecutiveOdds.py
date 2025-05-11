"""
LeetCode Problem: Three Consecutive Odds
Problem Number: 1550
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/three-consecutive-odds/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def threeConsecutiveOdds(self, arr):
        for idx in range(len(arr) - 2):
            if (arr[idx] % 2 == 1) and \
                (arr[idx + 1] % 2 == 1) and \
                (arr[idx + 2] % 2 == 1):
                return True
        return False

    # Counter
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def threeConsecutiveOdds(self, arr):
        odds = 0
        for idx in range(len(arr)):
            if arr[idx] % 2 == 1:
                odds += 1
                if odds == 3:
                    return True
            else:
                odds = 0
        return False
    
    # Product
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def threeConsecutiveOdds(self, arr):
        for idx in range(len(arr) - 2):
            if (arr[idx] * arr[idx+1] * arr[idx+2]) % 2 == 1:
                return True
        return False
