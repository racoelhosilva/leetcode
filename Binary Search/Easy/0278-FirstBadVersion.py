"""
LeetCode Problem: First Bad Version
Problem Number: 278
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    # Binary Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def firstBadVersion(self, n):
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
