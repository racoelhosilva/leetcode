"""
LeetCode Problem: Product of Array Except Self
Problem Number: 238
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums):
        res = []
        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if i != j:
                    cur *= nums[j]
            res.append(cur)
        return res

    # Prefix and Suffix Arrays
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums):
        res = [0] * len(nums) 
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
    
    # Prefix and Suffix Precomputation
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums):
        res = [1] * len(nums) 

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
