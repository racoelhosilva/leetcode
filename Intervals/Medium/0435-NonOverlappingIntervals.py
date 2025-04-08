"""
LeetCode Problem: Non Overlapping Intervals
Problem Number: 435
Difficulty: Medium
Topic: Intervals
Link: https://leetcode.com/problems/non-overlapping-intervals/
"""

class Solution:
    # Greedy Approach (Sort by Start)
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()

        res = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                res += 1
                prev = min(prev, end)
        return res

    # Greedy Approach (Sort by End)
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev:
                res += 1
            else:
                prev = end

        return res
