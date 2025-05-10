"""
LeetCode Problem: Minimum Equal Sum of Two Arrays After Replacing Zeros
Problem Number: 2918
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
"""

class Solution:
    # Greedy Replacements
    # Since all 0s have to be replaced, we can assume they are now 1s
    # The only case where it is not possible is when the array with smaller sum
    # did not have any 0s
    # Otherwise we will try to match the maximum of the arrays after replacing with 1s
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minSum(self, nums1, nums2):
        s1 = s2 = 0
        c1 = c2 = 0

        for num in nums1:
            if num == 0:
                c1 += 1
            else:
                s1 += num
        s1 += c1
        for num in nums2:
            if num == 0:
                c2 += 1
            else:
                s2 += num
        s2 += c2

        if (s1 < s2 and c1 == 0) or (s2 < s1 and c2 == 0):
            return -1
        return max(s1, s2)
