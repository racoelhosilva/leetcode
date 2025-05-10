"""
LeetCode Problem: Maximum Subsequence Score
Problem Number: 2542
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/maximum-subsequence-score/
"""

from heapq import heappop, heappush

class Solution:
    # Pairing + Min Heap
    # We want to find a balance between multiplier and running sum
    # For this, we can keep track of the values from both arrays with the same index
    # By sorting this in decreasing multiplier, we will always know which is the multiplier
    # Finally, we keep a running sum of the current index and the other k-1 largest values
    # At each step, we update the res if there are k elements in the heap
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def maxScore(self, nums1, nums2, k):

        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        runsum = 0
        res = 0

        for n2, n1 in pairs:
            runsum += n1
            heappush(heap, n1)
            if len(heap) == k:
                res = max(res, runsum * n2)
                runsum -= heappop(heap)

        return res
