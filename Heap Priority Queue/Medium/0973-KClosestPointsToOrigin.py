"""
LeetCode Problem: K Closest Points to Origin
Problem Number: 973
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/k-closest-points-to-origin/
"""

import heapq
from random import randint

class Solution:
    # Sorting
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def kClosest(self, points, k):
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    # Min-Heap
    # Time Complexity: O(n + k log n)
    # Space Complexity: O(n)
    def kClosest(self, points, k):
        def distance(point):
            x,y = point
            return (x ** 2 + y ** 2)
        heap = []
        for point in points:
            heap.append((distance(point), point))
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # Max-Heap
    # Time Complexity: O(n log k)
    # Space Complexity: O(n)
    def kClosest(self, points, k):
        def distance(point):
            x,y = point
            return (x ** 2 + y ** 2)
        heap = []
        for point in points:
            heapq.heappush((-distance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)
        return heap
    
    # Quick Select
    # This method is similar to the quicksort algorithm
    # We use l and r to define a partition space
    # In that partition space, we choose a pivot (randomly for better efficiency)
    # We are then going to partition the array into values smaller and larger than that pivot
    # We return the number of index of the pivot point, which determines how to reduce the partition space
    # If the partition was too large, reduce the search space with the r pointer
    # If the partition was too small, keep the r pointer and move the l pointer (marking values to the left as selected)
    # By repeating this process, p will eventually equal k, meaning that the first k elements are the smallest
    # Time Complexity: O(n) -> average; O(n^2) -> worst
    # Space Complexity: O(1)
    def kClosest(self, points, k):     
        def distance(point):
            x,y = point
            return (x ** 2 + y ** 2)
        
        def partition(l, r):
            pivotIdx = randint(l, r)
            pivotValue = distance(points[pivotIdx])
            points[r], points[pivotIdx] = points[pivotIdx], points[r]
            
            stored_index = l
            for i in range(l, r):
                if distance(points[i]) < pivotValue:
                    points[stored_index], points[i] = points[i], points[stored_index]
                    stored_index += 1
            points[r], points[stored_index] = points[stored_index], points[r] 
            return stored_index
        
        l, r, p = 0, len(points)-1, len(points)
        while p != k:
            p = partition(l, r)
            if p < k:   
                l = p + 1
            else:
                r = p - 1
        return points[:k]
