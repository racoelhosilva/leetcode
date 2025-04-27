"""
LeetCode Problem: Max Number of K Sum Pairs
Problem Number: 1679
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""

class Solution:
    # Sort + Two Pointers
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            temp = nums[l] + nums[r]
            if temp < k:
                l += 1
            elif temp > k:
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res
    
    # Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxOperations(self, nums, k):
        seen = dict()
        res = 0
        for num in nums:
            target = k - num
            if target in seen:
                seen[target] -= 1
                if seen[target] == 0:
                    del seen[target]
                res += 1
            else:
                seen[num] = seen.get(num, 0) + 1
        return res
