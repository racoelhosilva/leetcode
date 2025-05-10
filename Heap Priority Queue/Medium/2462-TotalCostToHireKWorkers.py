"""
LeetCode Problem: Total Cost to Hire K Workers
Problem Number: 2462
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/total-cost-to-hire-k-workers/
"""

class Solution:
    # Min heap of costs
    # Keep track of the min heap of costs, with candidates from head and tail
    # Repeat k times, popping the smallest and adding the respective one
    # Time Complexity: O((k + m) log m)
    # Space Complexity: O(m)
    def totalCost(self, costs, k, candidates):
        # Small improvement in some cases
        if candidates * 2 + k > len(costs):
            costs.sort()
            return sum(costs[:k])

        from heapq import heapify, heappop, heappush

        heap = []
        for i in range(candidates):
            heap.append((costs[i], i))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            heap.append((costs[i], i))
        heapify(heap)

        res = 0
        l, r = candidates, len(costs) - candidates - 1

        for _ in range(k):
            cost, idx = heappop(heap)
            res += cost
            if l <= r:
                if idx < l:
                    heappush(heap, (costs[l], l))
                    l += 1
                else:
                    heappush(heap, (costs[r], r))
                    r -= 1
        
        return res
