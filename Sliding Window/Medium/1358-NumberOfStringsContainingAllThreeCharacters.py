"""
LeetCode Problem: Number of Strings Containing All Three Characters
Problem Number: 1358
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/number-of-strings-containing-all-three-characters/
"""

class Solution:
    # Sliding Window
    # Initially expand the sliding window until all characters are contained within it
    # After that, reduce it until not all characters are contained
    # At each step, add n - r (all substrings that start with the current window)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfSubstrings(self, s):
        from collections import defaultdict
        freq = defaultdict(int)

        res = 0
        n = len(s)
        l = 0
        for r in range(n):
            freq[s[r]] += 1

            while len(freq) == 3:
                res += (n - r)
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    freq.pop(s[l])
                l += 1
        return res

    # Last Index Tracking
    # A simpler approach is to just initialize all indices at -1
    # At each step, we should update the last index of the current element
    # We can then add 1 + min(last_idx) 
    # This corresponds to the number of substrings containing every letter until now
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfSubstrings(self, s):
        last_idx = [-1] * 3
        res = 0
        for idx in range(len(s)):
            last_idx[ord(s[idx]) - ord('a')] = idx
            res += 1 + min(last_idx)
        return res
