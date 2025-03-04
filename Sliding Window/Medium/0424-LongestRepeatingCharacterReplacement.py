"""
LeetCode Problem: Longest Repeating Character Replacement
Problem Number: 424
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

class Solution:
    # Sliding Window
    # While we can keep expanding the solution, do so
    # When there are more characters needed to be replaced in the window than k,
    # Reduce the sliding window from the left until it is possible again
    # Update the result and continue moving the window
    # Time Complexity: O(n)
    # Space Complexity: O(m)
    def characterReplacement(self, s, k):
        res = 0
        
        from collections import defaultdict
        freq = defaultdict(int)
        max_freq = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
        
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)
        
        return res
