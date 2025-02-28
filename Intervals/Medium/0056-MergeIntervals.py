"""
LeetCode Problem: Merge Intervals
Problem Number: 56
Difficulty: Medium
Topic: Intervals
Link: https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    # Sort and Compare
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res
