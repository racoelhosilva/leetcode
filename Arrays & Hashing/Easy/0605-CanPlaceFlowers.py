"""
LeetCode Problem: Can Place Flowers
Problem Number: 605
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/can-place-flowers/
"""

class Solution:
    # One Pass
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canPlaceFlowers(self, flowerbed, n):
        for idx in range(len(flowerbed)):
            if flowerbed[idx] and \
                (idx == 0 or flowerbed[idx - 1] == 0) and \
                (idx == len(flowerbed - 1) or flowerbed[idx + 1] == 0):
                flowerbed[idx] = 1
                n -= 1
                if n <= 0:
                    return True
        return n <= 0