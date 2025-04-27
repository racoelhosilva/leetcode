"""
LeetCode Problem: String Compression
Problem Number: 443
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/string-compression/
"""

class Solution:
    # Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def compress(self, chars):
        l, r = 0, 0

        while r < len(chars):
            cur_char = chars[r]
            sequence_count = 0

            while r < len(chars) and chars[r] == cur_char:
                sequence_count += 1
                r += 1
            
            chars[l] = cur_char
            l += 1
            if sequence_count > 1:
                for char in str(sequence_count):
                    chars[l] = char
                    l += 1

        return l
