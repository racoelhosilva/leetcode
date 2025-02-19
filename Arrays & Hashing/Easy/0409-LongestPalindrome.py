"""
LeetCode Problem: Longest Palindrome
Problem Number: 409
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/longest-palindrome/
"""

class Solution:
    # Two-Pass Hash Table
    # The longest palindrome can be constructed by all pairs of the same letter
    # Additionally, we can have a single unpaired letter in the center
    # We can use dictionary to track the frequencies of each letter
    # Time Complexity: O(n)
    # Space Complexity: O(52) -> O(1)
    def longestPalindrome(self, s):
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        res = 0
        for v in freq.values():
            res += 2 * (v // 2)
            if v % 2 == 1 and res % 2 == 0:
                res += 1
        return res
    
    # One-Pass Hash Table
    # Instead of recalculating the palindrome size, keep track of which
    # letters are not part of the palindrome and subtract in the end
    # Time Complexity: O(n)
    # Space Complexity: O(52) -> O(1)
    def longestPalindrome(self, s):
        freq = dict()
        unpaired = 0
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] % 2 == 1:
                unpaired += 1
            else:
                unpaired -= 1
        if unpaired > 0:
            return len(s) - unpaired + 1
        else:
            return len(s)
        
    # Hash Set
    # Instead of keeping track of the frequencies of the letters, check if
    # they are unpaired (in the set) or not and update the total count
    # Time Complexity: O(n)
    # Space Complexity: O(52) -> O(1)
    def longestPalindrome(self, s):
        chars = set()
        res = 0
        for char in s:
            if char in chars:
                chars.remove(char)
                res += 2
            else:
                chars.add(char)
        if chars:
            res += 1
        return res    
