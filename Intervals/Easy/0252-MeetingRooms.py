"""
LeetCode Problem: Meeting Rooms
Problem Number: 252
Difficulty: Easy
Topic: Intervals
Link: https://leetcode.com/problems/meeting-rooms/
"""

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # Brute-Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def canAttendMeetings(self, intervals):
        for i in range(len(intervals)):
            a = intervals[i]
            for j in range(i + 1, len(intervals)):
                b = intervals[j]
                if a.start < b.start and b.start < a.end:
                    return False
                if b.start < a.start and a.start < b.end:
                    return False
        return True

    # Sorting
    # Instead of brute-forcing, we can start by sorting them by start time
    # After this, we just have to compare if the next interval conflicts with the current
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def canAttendMeetings(self, intervals):
        intervals = intervals.sort(lambda x: x.start)
        for idx in range(len(intervals)-1):
            if intervals[idx].end > intervals[idx].start:
                return False
        return True
