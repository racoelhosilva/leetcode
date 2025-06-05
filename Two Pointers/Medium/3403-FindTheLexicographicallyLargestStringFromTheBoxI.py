"""
LeetCode Problem: Find the Lexicographically Largest String From the Box I
Problem Number: 3403
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
"""

class Solution:
    # Enumeration
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        
        maxLen = len(word) - numFriends + 1
        return max(word[i:i+maxLen] for i in range(len(word)))

    # Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        
        # Adapted from problem 1163
        def lastSubstring(s):
            n = len(s)
            i, j, k = 0, 1, 0
            while j + k < n:
                if s[i + k] == s[j + k]:
                    k += 1
                else:
                    if s[i + k] > s[j + k]:
                        j += k + 1
                    else:
                        i = max(i + k + 1, j)
                        j = i + 1
                    k = 0
            return s[i:]
        
        last = lastSubstring(word)
        return last[:min(len(last), len(word) - numFriends + 1)]
