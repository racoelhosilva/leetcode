"""
LeetCode Problem: Longest Substring Without Repeating Characters
Problem Number: 3
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    # Sliding Window (Hash Set)
    # While the char hasn't been seen yet, increase the window
    # If the char is repeated, decrease the window until it is removed
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s):
        chars = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        
        return res

    # Sliding Window (Hash Table)
    # This solutions is slightly better because the l pointer moves with larger steps
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s):
        chars = dict()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)
            chars[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res

