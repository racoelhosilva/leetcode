"""
LeetCode Problem: Meeting Rooms II
Problem Number: 253
Difficulty: Medium
Topic: Intervals
Link: https://leetcode.com/problems/meeting-rooms-ii/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def minMeetingRooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s = e = 0
        res = rooms = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            res = max(res, rooms)
        return res

    # Sort timestamps
    # The number of rooms will be maximum count of overlapping meetings
    # If we pick all the timestamps and sort them by time (giving priority to end)
    # We just need to iterate through keeping a count of the current rooms
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def minMeetingRooms(self, intervals):
        timestamps = []
        for interval in intervals:
            timestamps.append((interval[0], 1))
            timestamps.append((interval[1], -1))
        timestamps.sort(lambda timestamp: (timestamp[0], timestamp[1]))
        res = rooms = 0
        for t in timestamps:
            rooms += t[1]
            res = max(res, rooms)
        return res
