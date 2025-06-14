"""
LeetCode Problem: Maximum Difference by Remapping a Digit
Problem Number: 2566
Difficulty: Easy
Topic: Greedy
Link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
"""

class Solution:
    # Greedy Replacement
    # Time Complexity: O(d)
    # Space Complexity: O(d)
    def minMaxDifference(self, num):
        mx = mn = str(num)
        
        pos = 0
        while pos < len(mx) and mx[pos] == '9':
            pos += 1
        if pos < len(mx):
            mx.replace(mx[pos], '9')
        
        mn.replace(mn[0], '0')

        return int(mx) - int(mn)
