"""
LeetCode Problem: Top K Frequent Elements
Problem Number: 347
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/top-k-frequent-elements/
"""

class Solution:
    # Sort by Frequency
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums, k):
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = freq.items()
        freq.sort(key=lambda pair: pair[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freq[i][0])
        return res
    
    # Heap
    # Time Complexity: O(n log k)
    # Space Complexity: O(n + k)
    def topKFrequent(self, nums, k):
        import heapq
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for key, val in freq:
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
    # Quick Select
    # Apply the quick select algorithm based on the unique values and their frequencies
    # Time Complexity: O(n) -> average; O(n^2) -> worst
    # Space Complexity: O(1)
    def topKFrequent(self, nums, k):
        from random import randint
        
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        unique = list(freq.keys())

        def partition(l, r):
            pivot_idx = randint(l, r)
            pivot_value = freq[unique[pivot_idx]]
            unique[r], unique[pivot_idx] = unique[pivot_idx], unique[r]

            stored_index = l
            for i in range(l, r):
                if freq[unique[i]] < pivot_value:
                    unique[i], unique[stored_index] = unique[stored_index], unique[i]
                    stored_index += 1
            unique[r], unique[stored_index] = unique[stored_index], unique[r]
            return stored_index 

        n = len(unique)
        l, r, p = 0, n-1, n
        while p != n - k:
            p = partition(l, r)
            if p < n - k:
                l = p + 1
            else:
                r = p - 1
        return unique[n-k:]

    # Bucket Sort
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums, k):
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [] * (len(nums) + 1)
        for key, value in freq.items():
            buckets[value].append(key)
        res = []
        for idx in range(len(buckets) - 1, 0, -1):
            for num in buckets[idx]:
                res.append(num)
                if len(res) == k:
                    return res
