"""
LeetCode Problem: Minimum Number of Arrows to Burst Balloons
Problem Number: 452
Difficulty: Medium
Topic: Intervals
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""

class Solution:
    # Greedy Approach (Sort by Start)
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def findMinArrowShots(self, points):
        points.sort(key=lambda balloon: balloon[0])
        arrow = points[0][1]
        res = 1

        for i in range(1, len(points)):
            if points[i][0] > arrow:
                res += 1
                arrow = points[i][1]
            else:
                arrow = min(arrow, points[i][1])

        return res
    
    # Greedy Approach (Sort by End)
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def findMinArrowShots(self, points):
        points.sort(key=lambda balloon: balloon[1])
        arrow = points[0][1]
        res = 1

        for i in range(1, len(points)):
            if points[i][0] < arrow:
                res += 1
                arrow = points[i][1]
        return res
