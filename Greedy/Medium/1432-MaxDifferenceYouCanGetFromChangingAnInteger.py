"""
LeetCode Problem: Max Difference You Can Get From Changing an Integer
Problem Number: 1432
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
"""

class Solution:
    # Greedy Replacement
    # Time Complexity: O(d)
    # Space Complexity: O(d)
    def maxDiff(self, num):
        mx, mn = str(num), str(num)

        # Replace the first non-9 digit if any
        pos = 0
        while pos < len(mx) and mx[pos] == '9':
            pos += 1
        if pos < len(mx):
            mx = mx.replace(mx[pos], '9')

        if mn[0] != "1":
            # Replace the first digit if it's not-1 by 1
            mn = mn.replace(mn[0], '1')
        else:
            # Find the first digit that is not-0 (minimum) or not-1 (first-digit) by 0
            pos = 1
            while pos < len(mn) and (mn[pos] == '0' or mn[pos] == '1'):
                pos += 1
            if pos < len(mn):
                mn = mn.replace(mn[pos], '0')
        
        return int(mx) - int(mn)
