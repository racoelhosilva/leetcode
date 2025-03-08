"""
LeetCode Problem: Permutation in String
Problem Number: 567
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/permutation-in-string/
"""

class Solution:
    # Sliding Window + Frequency Array of Chars
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        freq = [0] * 26
        window = [0] * 26
        for r in range(m):
            freq[ord(s1[r]) - ord('a')] += 1
            window[ord(s2[r]) - ord('a')] += 1

        if freq == window:
            return True

        for r in range(m, n):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r - m]) - ord('a')] += 1

            if freq == window:
                return True
        
        return False
    
    # Sliding Window + Frequency Array of Chars (Optimal)
    # By keeping track of the match count, we can optimized the code
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        freq = [0] * 26
        window = [0] * 26
        match_count = 0

        for r in range(m):
            freq[ord(s1[r]) - ord('a')] += 1
            window[ord(s2[r]) - ord('a')] += 1

        for i in range(26):
            if freq[i] == window[i]:
                match_count += 1

        for r in range(m, n):
            if match_count == 26:
                return True

            # Add new char to window
            index_new = ord(s2[r]) - ord('a')
            window[index_new] += 1
            if window[index_new] == freq[index_new]:
                match_count += 1
            elif window[index_new] == freq[index_new] + 1:
                match_count -= 1

            # Remove old char from window
            index_old = ord(s2[r-m]) - ord('a')
            window[index_old] -= 1
            if window[index_old] == freq[index_old]:
                match_count += 1
            elif window[index_old] == freq[index_old] - 1:
                match_count -= 1
        
        return match_count == 26
