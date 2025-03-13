"""
LeetCode Problem: Find the Difference of Two Arrays
Problem Number: 2215
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
"""

class Solution:
    # Hash Sets
    # Time Complexity: O(N + M)
    # Space Complexity: O(N + M)
    def findDifference(self, nums1, nums2):
        res = [[], []]
        uniq1 = set()
        for num in nums1:
            uniq1.add(num)
        
        uniq2 = set()
        for num in nums2:
            uniq2.add(num)

        for num in uniq1:
            if num in uniq2:
                uniq2.remove(num)
            else:
                res[0].append(num)
        
        for num in uniq2:
            res[1].append(num)
        
        return res

    # Python Shorthands
    # Time Complexity: O(N + M)
    # Space Complexity: O(N + M)
    def findDifference(self, nums1, nums2):
        uniq1 = set(nums1)
        uniq2 = set(nums2)
        return [list(uniq1.difference(uniq2)), list(uniq2.difference(uniq1))]
