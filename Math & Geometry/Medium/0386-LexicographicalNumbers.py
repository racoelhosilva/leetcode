"""
LeetCode Problem: Lexicographical Numbers
Problem Number: 386
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/lexicographical-numbers/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n + log n)
    def lexicalOrder(self, n):
        res = []

        def dfs(cur):
            res.append(cur)
            for digit in range(10):
                nxt = cur * 10 + digit
                if nxt <= n:
                    dfs(nxt)
                else:
                    break
        
        for cur in range(1, min(10, n+1)):
            dfs(cur)

        return res


    # Iterative Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n), O(1) additional space
    def lexicalOrder(self, n):
        res = []
        cur = 1

        for _ in range(n):
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur >= n or cur % 10 == 9:
                    cur //= 10
                cur += 1

        return res
    
    # Python One-liner
    def lexicalOrder(self, n):
        return map(int, sorted(map(str, range(1,n+1))))
