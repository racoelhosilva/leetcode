"""
LeetCode Problem: Permutations
Problem Number: 46
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/permutations/
"""

class Solution:
    # Backtracking
    # Backtrack through the indices of the list
    # Swap element in that position with every other element
    # Time Complexity: O(n! * n)
    # Space Complexity: O(n! * n)
    def permute(self, nums):
        res = []

        def backtrack(idx, sequence):
            if idx == len(sequence):
                res.append(sequence[:])
                return

            for j in range(idx, len(sequence)):
                sequence[idx], sequence[j] = sequence[j], sequence[idx]
                backtrack(idx + 1, sequence)
                sequence[idx], sequence[j] = sequence[j], sequence[idx]                

        backtrack(0, nums)
        return res

