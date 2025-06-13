"""
LeetCode Problem: Minimize the Maximum Difference of Pairs
Problem Number: 2616
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
"""

class Solution:
    # Sort + Binary Search + Greedy
    # By initially sorting the array, we ensure that the pair comparison can be made by adjacent elements
    # For any ordered array, the maximum number of pairs with difference less than k can be chosen greedily
    # By binary searching the possible k values, we can quickly 
    # converge to the minimum difference that contains p pairs
    # The trick is in flipping the script and given a fixed difference, 
    # find how many pairs can be made that share less than that difference
    # and then selecting the smallest difference that has at least p pairs
    # Time Complexity: O(n log n + n log m)
    # Space Complexity: O(1)
    def minimizeMax(self, nums, p):
        if p == 0:
            return 0
        n = len(nums)
        nums = sorted(nums)
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = (l + r) >> 1
            
            cnt = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= m:
                    cnt += 1
                    i += 1
                i += 1
            
            if cnt >= p:
                r = m
            else:
                l = m + 1
        
        return l
