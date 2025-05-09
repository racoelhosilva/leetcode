"""
LeetCode Problem: Next Permutation
Problem Number: 31
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/next-permutation/
"""

class Solution:
    # Find, Swap, Reverse
    # Find first decreasing element from right -> left
    # Swap it with the smallest larger element from right
    # Reverse everything on the right (to make it increasing)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
