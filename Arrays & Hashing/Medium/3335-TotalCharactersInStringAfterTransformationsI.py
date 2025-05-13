"""
LeetCode Problem: Total Characters in String After Transformations I
Problem Number: 3335
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
"""

class Solution:
    # Full transformation simulation
    # Time Complexity: O(n + t)
    # Space Complexity: O(1)
    def lengthAfterTransformations(self, s, t):
        mod = 1**9 +  7
        freq = [0] * 26
        nxt = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        for _ in range(t):
            nxt[0] = freq[25]
            nxt[1] = (freq[25] + freq[0]) % mod
            for idx in range(2, 26):
                nxt[idx] = freq[idx-1]
            freq, nxt = nxt, freq
        return sum(freq) % mod
    
    # Deque Optimization
    # Time Complexity: O(n + t)
    # Space Complexity: O(1)
    def lengthAfterTransformations(self, s, t):
        from collections import deque

        mod = 10**9 + 7
        arr = [0] * 26
        orda = ord("a")
        for char in s:
            arr[ord(char) - orda] += 1
        
        freq = deque(arr)
        for _ in range(t):
            freq.appendleft(freq.pop())
            freq[1] += (freq[0] % mod) 
        return sum(freq) % mod 
