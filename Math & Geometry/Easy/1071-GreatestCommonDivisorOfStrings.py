"""
LeetCode Problem: Greatest Common Divisor of Strings
Problem Number: 1071
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""

class Solution:
    # GCD + verification
    # This problem might seem deceptively hard, but for the strings to have a gcd, 
    # They must be repetitions of smaller strings
    # This means that the gcd of their length is the size of the largest string that can be repeated
    # to form the strings str1 and str2
    # After obtaining the gcd, we just need to check that both strings are repeat the pattern % g
    # Time Complexity: O(m + n)
    # Space Complexity: O(g)
    def gcdOfStrings(self, str1, str2):
        # Time Complexity: O(log min(a,b))
        # Space Complexity: O(1)
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        g = gcd(len(str1), len(str2))
        
        for i in range(len(str1)):
            if str1[i] != str1[i % g]:
                return ""

        for i in range(len(str2)):
            if str2[i] != str1[i % g]:
                return ""

        return str1[:g]

    # GCD + verification
    # A similar check could also be made by checking the concatenation of the strings
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def gcdOfStrings(self, str1, str2):
        # Time Complexity: O(log min(a,b))
        # Space Complexity: O(1)
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""
        g = gcd(len(str1), len(str2))
        return str1[:g]
