"""
LeetCode Problem: Divide Array Into Arrays With Max Difference
Problem Number: 2966
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
"""

class Solution:
    # Sort + Greedy
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def divideArray(self, nums, k):
        res = []
        nums.sort()

        for idx in range(0, len(nums), 3):
            if nums[idx+2] - nums[idx] > k:
                return []
            res.append([nums[idx], nums[idx+1], nums[idx+2]])
        return res
