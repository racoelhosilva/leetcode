"""
LeetCode Problem: Palindrome Partitioning
Problem Number: 131
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/palindrome-partitioning/
"""

class Solution:
    # Backtracking 
    # Time Complexity: O(n * 2 ^ n)
    # Space Complexity: O(n * 2 ^ n)
    def partition(self, s):
        res = []
        n = len(s)

        def check_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(i, cur):
            if i >= n:
                res.append(cur[:])
                return
            
            for j in range(i, n):
                if check_palindrome(i, j):
                    cur.append(s[i:j+1])
                    backtrack(j+1, cur)
                    cur.pop()

        backtrack(0, [])
        return res
