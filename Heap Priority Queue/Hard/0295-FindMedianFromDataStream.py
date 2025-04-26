"""
LeetCode Problem: Find Median from Data Stream
Problem Number: 295
Difficulty: Hard
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/find-median-from-data-stream/
"""

import heapq

# Two Heap Solution
# Space Complexity: O(n)
class MedianFinder(object):

    # Initializing two heaps
    # Left: keeps track of largest element in left side of sorted array (max-heap)
    # Right: keeps track of smaller element in right side of sorted array (min-heap)
    # The two heaps should be kept more or less balanced
    def __init__(self):
        self.left = []
        self.right = []

    # Adds a number to the Data Stream
    # Time Complexity: O(log n)
    def addNum(self, num):
        nl, nr = len(self.left), len(self.right)
        
        # There are more elements on the left
        if nl > nr:
            # If the new element is smaller than the largest of the left,
            # there has to be a replacement
            if -self.left[0] > num:
                heapq.heappush(self.right, -heapq.heapreplace(self.left, -num))
            # Else, the element can just be added to the right
            else:
                heapq.heappush(self.right, num)
        
        # There are more elements on the right
        elif nr > nl:
            # If the new element is larger than the smalles of the right,
            # there has to be a replacement
            if self.right[0] < num:
                heapq.heappush(self.left, -heapq.heapreplace(self.right, num))
            # Else, the element can just be added to the left
            else:
                heapq.heappush(self.left, -num)
        
        # The number of elements is the same
        else:
            # If the element is smaller than the smallest of the left,
            # push it there
            if self.left and -self.left[0] > num:
                heapq.heappush(self.left, -num)
            # Else, push the element to the right
            # This makes it slightly right-biased
            else:
                heapq.heappush(self.right, num)

    # Obtain Median of Stream
    # Time Complexity: O(1)
    def findMedian(self):
        nl, nr = len(self.left), len(self.right)
        # If there are more elements on the left,
        # return largest element
        if nl > nr:
            return -self.left[0]
        # If there are more elements on the right,
        # return smallest element
        elif nr > nl:
            return self.right[0]
        # Else, return mean of both previous values
        else:
            return (-self.left[0] + self.right[0]) * 1.0 / 2
