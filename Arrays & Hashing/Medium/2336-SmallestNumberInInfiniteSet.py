"""
LeetCode Problem: Smallest Number in Infinite Set
Problem Number: 2336
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/smallest-number-in-infinite-set/
"""

from heapq import heappop, heappush

# Min Heap and Set
# Space Complexity: O(k)
class SmallestInfiniteSet:
    # Initialize the structure
    def __init__(self):
        self.cur = 1
        self.heap = []
        self.back = set()

    # Pop smallest element
    # Time Complexity: O(log k)
    def popSmallest(self):
        if self.heap:
            self.back.remove(self.heap[0])
            return heappop(self.heap)
        res = self.cur
        self.cur += 1
        return res

    # Add back a smaller element
    # Time Complexity: O(log k)
    def addBack(self, num):
        if num < self.cur and num not in self.back:
            heappush(self.heap, num)
            self.back.add(num)
