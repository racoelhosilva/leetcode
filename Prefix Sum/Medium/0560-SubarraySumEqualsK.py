"""
LeetCode Problem: Subarray Sum Equals K
Problem Number: 560
Difficulty: Medium
Topic: Prefix Sum
Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""

class Solution:
    # Naive Approach
    # Time Complexity: O(n^2) -> TLE
    # Space Complexity: O(1)
    def subarraySum(self, nums, k):
        res = 0
        for start in range(len(nums)):
            cur = 0
            for end in range(start, len(nums)):
                cur += nums[end]
                if cur == k:
                    res += 1
        return res

    def subarraySum(self, nums, k):
        prev = {0:1}
        res = cur = 0

        for num in nums:
            cur += num
            if cur - k in prev:
                res += prev[cur - k]
            if cur in prev:
                prev[cur] += 1
            else:
                prev[cur] = 1

        return res 
