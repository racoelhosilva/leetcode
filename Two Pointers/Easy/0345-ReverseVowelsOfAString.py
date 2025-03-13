"""
LeetCode Problem: Reverse Vowels of a String
Problem Number: 345
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(n) -> Python strings are immutable
    def reverseVowels(self, s):
        word = list(s)
        l, r = 0, len(s) - 1
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
        return "".join(word)
