"""
LeetCode Problem: Merge Sorted Array
Problem Number: 88
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    # Two Pointers
    # Merge sorted from the end of the arrays
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def merge(self, nums1, m, nums2, n):
        m -= 1
        n -= 1
        while n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m+n] = nums1[m]
                m -= 1
            else:
                nums1[m+n] = nums2[n]
                n -= 1
