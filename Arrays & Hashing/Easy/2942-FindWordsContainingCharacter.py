"""
LeetCode Problem: Find Words Containing Character
Problem Number: 2942
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/find-words-containing-character/
"""

class Solution:
    # Simulation
    # Time Complexity: O(n * m)
    # Space Complexity: O(n)
    def findWordsContaining(self, words, x):
        res = []
        for idx in range(len(words)):
            if x in words[idx]:
                res.append(idx)
        return res
