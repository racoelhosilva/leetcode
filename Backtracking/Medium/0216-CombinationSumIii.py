"""
LeetCode Problem: Combination Sum III
Problem Number: 216
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/combination-sum-iii/
"""

class Solution:
    # Bcaktracking
    # Time Complexity: O(C(9, k))
    # Space Complexity: O(k * C(9, k))
    def combinationSum3(self, k, n):
        res = []

        def backtrack(num, cur, s, l):
            if l == k and s == n:
                res.append(cur[:])
                return
            
            if l >= k:
                return 

            for i in range(num, 10):
                if s + i > n:
                    return
                cur.append(i)
                backtrack(i + 1, cur, s + i, l + 1)
                cur.pop()

        backtrack(1, [], 0, 0)
        return res
