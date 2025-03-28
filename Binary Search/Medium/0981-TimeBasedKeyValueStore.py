"""
LeetCode Problem: Time Based Key Value Store
Problem Number: 981
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/time-based-key-value-store/
"""

# Hashmap of Keys to List of (Timestamp, Values)
# Space Complexity: O(k * v)
class TimeMap:

    # Initialize the structure
    def __init__(self):
        from collections import defaultdict
        self.hashmap = defaultdict(list)

    # Add a new element
    # Time Complexity: O(1)
    def set(self, key, value, timestamp):
        self.hashmap[key].append((timestamp, value))

    # Retrieve an element
    # Time Complexity: O(log n)
    def get(self, key, timestamp):
        values = self.hashmap[key]
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
