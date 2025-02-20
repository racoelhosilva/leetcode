"""
LeetCode Problem: Squares of a Sorted Array
Problem Number: 977
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    # Naive Approach
    # Square each element and sort the array
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def sortedSquares(self, nums):
        res = [n*n for n in nums]
        return sorted(res)
    
    # Two Pointers
    # Keep an array at the start and end of the list
    # Check which square will be larger and fill result in reverse
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def sortedSquares(self, nums):
        left, right = 0, len(nums)-1
        res = [0] * len(nums)
        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                res[right-left] = nums[left] * nums[left]
                left += 1
            else:
                res[right-left] = nums[right] * nums[right]
                right -= 1
        return nums
