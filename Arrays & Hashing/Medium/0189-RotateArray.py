"""
LeetCode Problem: Rotate Array
Problem Number: 189
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/rotate-array/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(n * k) -> TLE
    # Space Complexity: O(1)
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        while k:
            prev = nums[n-1]
            for i in range(n):
                nums[i], prev = prev, nums[i]
            k -= 1
    
    # Extra space
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        nums[:] = rotated

    # Block Swap
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def rotate(self, nums, k):
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]

    # Cyclic Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        swaps = start = 0
        while swaps < n:
            cur = start
            prev = nums[cur]
            while True:
                next_idx = (cur + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                cur = next_idx
                swaps += 1

                if start == cur:
                    break
            
            start += 1

    # Reversing blocks
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
            
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
