"""
LeetCode Problem: Detect Squares
Problem Number: 2013
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/detect-squares/
"""

# Geometry + Hash Map
# Space Complexity: O(n)
class DetectSquares:

    # Initialize hash map
    def __init__(self):
        self.points = dict()

    # Add new point to hash map
    # Time Complexity: O(1)
    def add(self, point):
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1

    # Obtain count of squares with point
    # Uses the diagonal property of a square
    # Time Complexity: O(n)
    def count(self, point):
        res = 0
        a,b = point
        for (x, y) in self.points:
            dx = a - x
            dy = b - y
            if (dx == dy or dx == -dy) and not (dx == 0 or dy == 0):
                res += self.points[(x,y)] * self.points.get((a,y), 0) * self.points.get((x,b), 0)
        return res
