"""
LeetCode Problem: Verifying an Alien Dictionary
Problem Number: 935
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

class Solution:
    # Hash Map
    # Create the match between a char in the alien alphabet and its index
    # Pay attention to substrings and length
    # When a first case of ordering is found, we can immediately move on to next case
    # Time Complexity: O(m * n)
    # Space Complexity: O(26) -> O(1)
    def isAlienSorted(self, words, order):
        match = {char:idx for idx, char in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if match[words[i][j]] > match[words[i+1][j]]:
                    return False
                elif match[words[i][j]] < match[words[i+1][j]]:
                    break
        return True