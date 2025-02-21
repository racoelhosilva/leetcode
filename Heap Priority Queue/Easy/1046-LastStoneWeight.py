"""
LeetCode Problem: Last Stone Weight
Problem Number: 1046
Difficulty: Easy
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/last-stone-weight/
"""

import heapq

class Solution:
    # Heap
    # Keep track of stones in a heap
    # At each stage, take out the two largest and smash them
    # Repeat until one or no stones left
    # Note: heapq always uses min-heap so values are converted
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        return stones[0] if stones else 0

