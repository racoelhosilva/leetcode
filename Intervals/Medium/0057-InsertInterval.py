"""
LeetCode Problem: Insert Interval
Problem Number: 57
Difficulty: Medium
Topic: Intervals
Link: https://leetcode.com/problems/insert-interval/
"""

class Solution:
    # Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:        
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        
        res.append(newInterval)
        return res