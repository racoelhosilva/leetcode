"""
LeetCode Problem: Count Largest Group
Problem Number: 1399
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/count-largest-group/
"""

class Solution:
    # Track possible sums
    # Time Complexity: O(n log n)
    # Space Complexity: O(log n)
    def countLargestGroup(self, n):
        from collections import defaultdict
        freqs = defaultdict(int)
        
        def digitSum(x):
            res = 0
            while x != 0:
                res += x % 10
                x //= 10
            return res

        for num in range(1, n + 1):
            val = digitSum(num)    
            freqs[val] += 1
        
        res = 0
        maxVal = 0
        for val in freqs.values():
            if val > maxVal:
                maxVal = val
                res = 1
            elif val == maxVal:
                res += 1
        return res
