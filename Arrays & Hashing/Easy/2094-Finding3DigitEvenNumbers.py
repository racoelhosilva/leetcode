"""
LeetCode Problem: Finding 3 Digit Even Numbers
Problem Number: 2094
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/finding-3-digit-even-numbers/
"""

class Solution:
    # Frequency + Enumeration
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def findEvenNumbers(self, digits):
        freqs = [0] * 10
        for digit in digits:
            freqs[digit] += 1
        
        res = []
        for a in range(1, 10):
            if freqs[a] > 0:
                freqs[a] -= 1
                for b in range(10):
                    if freqs[b] > 0:
                        freqs[b] -= 1
                        for c in range(0, 10, 2):
                            if freqs[c] > 0:
                                res.append(a * 100 + b * 10 + c)
                        freqs[b] += 1
                freqs[a] += 1
        return res
