"""
LeetCode Problem: Find Pivot Index
Problem Number: 724
Difficulty: Easy
Topic: Prefix Sum
Link: https://leetcode.com/problems/find-pivot-index/
"""

class Solution:
    # Prefix and Suffix Sum Arrays
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def pivotIndex(self, nums):
        n = len(nums)
        
        prefixSum = [0] * n
        suffixSum = [0] * n
        for i in range(1, n):
            prefixSum[i] = nums[i-1] + prefixSum[i-1]
            suffixSum[n - i - 1] = nums[n-i] + suffixSum[n-i]
        
        for idx in range(n):
            if prefixSum[idx] == suffixSum[idx]:
                return idx
        return -1

    # Prefix and Suffix Sums
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def pivotIndex(self, nums):
        total = sum(nums)
        prefixSum = 0

        for idx in range(len(nums)):
            suffixSum = total - prefixSum - nums[idx]
            if prefixSum == suffixSum:
                return idx
            prefixSum += nums[idx]
        return -1
