"""
LeetCode Problem: Longest Consecutive Sequence
Problem Number: 128
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    # Sort + Linear Search
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def longestConsecutive(self, nums):
        nums.sort()
        res = 0
        cur, streak = 0, 0
        i = 0
        while i < len(nums):
            if cur != nums[i]:
                cur = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == cur:
                i += 1
            streak += 1
            cur += 1
            res = max(res, streak)
        return res

    # Hash Map
    # Keep updating the limits of the streaks
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums):
        from collections import defaultdict
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if mp[num] == 0:
                mp[num] = mp[num-1] + mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
                res = max(res, mp[num])
        return res

    # Hash Set
    # Assume number is start of sequence and search until the end
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                streak = 1
                while num + streak in nums:
                    streak += 1
                res = max(res, streak)
        return res
