"""
LeetCode Problem: Kth Largest Element in a Stream
Problem Number: 703
Difficulty: Easy
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

import heapq
# https://docs.python.org/3/library/heapq.html

# Min Heap
# To keep track of the k-th largest element, we can use a min heap
# and force its maximum size to be k
# Time Complexity: O(n log k)
# Space Complexity: O(k)
class KthLargest:

    # Initialize the heap
    # Time Complexity: O(n log k)
    # Space Complexity: O(k)
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    # Add element and retrieve k-th largest
    # Time Complexity: O(log k)
    # Space Complexity: O(1)
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
