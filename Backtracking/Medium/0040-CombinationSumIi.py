"""
LeetCode Problem: Combination Sum II
Problem Number: 40
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    # Bcaktracking Optimal
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(cur, chosen, total):
            if total == target:
                res.append(chosen[:])
                return
            
            for idx in range(cur, len(candidates)):
                if idx != cur and candidates[idx] == candidates[cur]:
                    continue
                if total + candidates[idx] > target:
                    return
                chosen.append(candidates[idx])
                backtrack(idx + 1, chosen, total + candidates[idx])
                chosen.pop()

        backtrack(0, [], 0)
        return res
