"""
LeetCode Problem: 3Sum
Problem Number: 15
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/3sum/
"""

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    def threeSum(self, nums):
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return [list(x) for x in res]

    # Two Pointers
    # Since we will never get lower than n^2, sorting the array is useful
    # Fix an initial value and from there, search pairs of solutions using two pointers
    # When a solution is found, make sure that solution will not be repeated
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
