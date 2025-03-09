"""
LeetCode Problem: Combination Sum
Problem Number: 39
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/combination-sum/
"""

class Solution:
    # Backtracking
    # The complexity depends on the max number of elements in chosen
    # This is, at most, the target / minimum candidate
    # Time Complexity: O(2 ^ (t / min))
    # Space Complexity: O(t / min)
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(cur, chosen, total):
            if total == target:
                res.append(chosen[:])
                return
            if cur >= len(candidates) or total > target:
                return
            
            chosen.append(candidates[cur])
            backtrack(cur, chosen, total + candidates[cur])
            chosen.pop()
            backtrack(cur + 1, chosen, total)
        
        backtrack(0, [], 0)
        return res
    
    # Backtracking Optimal
    # By initially sorting the candidates, instead of testing every set
    # After the first set larger than target, we can return
    # Time Complexity: O(2^(t / min))
    # Space Complexity: O(t / min)
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(cur, chosen, total):
            if total == target:
                res.append(chosen[:])
                return
            
            for idx in range(cur, len(candidates)):
                if total + candidates[idx] > target:
                    return
                chosen.append(candidates[idx])
                backtrack(idx, chosen, total + candidates[idx])
                chosen.pop()
        
        backtrack(0, [], 0)
        return res
