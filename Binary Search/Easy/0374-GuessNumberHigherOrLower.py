"""
LeetCode Problem: Guess Number Higher or Lower
Problem Number: 374
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/guess-number-higher-or-lower/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pass

class Solution:
    # Binary Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def guessNumber(self, n):
        low, high = 1, n
        while low <= high:
            mid = (low + high) >> 1
            if guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid + 1
            else:
                return mid
    
    # Ternary Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def guessNumber(self, n):
        low, high = 1, n
        while low <= high:
            mid1 = low + (high-low) // 3
            mid2 = high - (high-low) // 3
            if guess(mid1) == 0:
                return mid1
            if guess(mid2) == 0:
                return mid2
            if guess(mid1) == 1:
                low = mid1 + 1
            if guess(mid2) == -1:
                high = mid2 - 1
