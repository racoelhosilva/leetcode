"""
LeetCode Problem: Kth Largest Element in an Array
Problem Number: 215
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq
from random import randint

class Solution:
    # Sorting and Selecting
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]

    # Quickselect
    # Due to the worst case complexity, this is not a possible solution to the problem
    # Time Complexity: O(n) -> average; O(n^2) -> worst
    # Space Complexity: O(1)
    def findKthLargest(self, nums, k):
        def partition(l, r):
            pivot_idx = randint(l, r)
            pivot_value = nums[pivot_idx]
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]

            stored_index = l
            for i in range(l, r):
                if nums[i] < pivot_value:
                    nums[i], nums[stored_index] = nums[stored_index], nums[i]
                    stored_index += 1
            nums[r], nums[stored_index] = nums[stored_index], nums[r]

            return stored_index
    
        n = len(nums)
        l, r, p = 0, n - 1, n
        while p != n - k:
            p = partition(l, r)
            if p < (n-k):
                l = p + 1
            else:
                r = p - 1
        return nums[p] 

    # Min Heap
    # Time Complexity: O(n log k)
    # Space Complexity: O(k)
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
