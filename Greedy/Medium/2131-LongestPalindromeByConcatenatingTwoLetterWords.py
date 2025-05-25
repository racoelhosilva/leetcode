"""
LeetCode Problem: Longest Palindrome by Concatenating Two Letter Words
Problem Number: 2131
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
"""

class Solution:
    # Frequency Matrix + One Pass Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestPalindrome(self, words):
        freqs = [[0] * 26 for _ in range(26)]
        res = 0
        for word in words:
            a, b = ord(word[0]) - ord('a'), ord(word[1]) - ord('a')
            if freqs[b][a]:
                res += 4
                freqs[b][a] -= 1
            else:
                freqs[a][b] += 1
        for i in range(26):
            if freqs[i][i]:
                res += 2
                break
        return res

    # Frequency Hash Map + Two Pass Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestPalindrome(self, words):
        freqs = {}
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
        
        res = 0
        odd = False
        for word, freq in freqs.items():
            if word[0] != word[1]:
                rev = word[::-1]
                if rev in freqs:
                    n = min(freq, freqs[rev])
                    res += n * 4
                    freqs[rev] = 0
                freqs[word] = 0
            else:
                if freq % 2 == 0:
                    res += freq * 2
                else:
                    res += (freq - 1) * 2
                    odd = True
        if odd:
            res += 2
        return res
