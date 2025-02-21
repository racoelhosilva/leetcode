"""
LeetCode Problem: Sum of All Subset XOR Totals
Problem Number: 1863
Difficulty: Easy
Topic: Backtracking
Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
"""

class Solution:
    # Generating All Subsets
    # A naive approach would be to generate all the subsets and simulate the problem
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(1)
    def subsetXORSum(self, nums):
        res = 0
        for mask in range(1 << len(nums)):
            xor = 0
            for idx in range(len(nums)):
                if mask & (1 << idx):
                    xor ^= nums[idx]
            res += xor
        return res
    
    # Backtracking Optimization
    # A better approach would be to perform the operations while backtracking
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def subsetXORSum(self, nums):
        def backtrack(idx, res):
            if idx == len(nums):
                return res
            return backtrack(idx+1, res ^ nums[idx]) + backtrack(idx+1, res)
        return backtrack(0, 0)

    # Bit Manipulation
    # An even better approach requires bit manipulation
    # Considering a number from nums, we know that it will be present in half of the subsets
    # After some analysis, we see that every place where a bit is set in one of the numbers in the original set
    # That same bit will be present in half of the subsets (since we are XOR'ing, those bits are just flipped)
    # So, if for every bit present in the original set, we know it will appear half the times in the end, 
    # The final sum will include the sum of that bit half the number of subsets, which is the same as the multiplication
    # of that bit with the length of the original subset minus 1
    # Therefore, we can replicate this by performing OR's with every element and then multiplying by half the number of subsets
    # which is the same as left shifting by length of original set - 1
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def subsetXORSum(self, nums):
        res = 0
        for num in nums:
            res |= num
        return res << (len(nums) - 1)
