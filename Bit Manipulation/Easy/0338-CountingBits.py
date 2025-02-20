"""
LeetCode Problem: Counting Bits
Problem Number: 338
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/counting-bits/
"""

class Solution:
    # Counting the bits (Brute-Force)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n):
        res = []
        for num in range(n + 1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res

    # Counting the bits (Bit Manipulation)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n):
        res = []
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num &= (num - 1)
        return res

    # Queue
    # The binary numbers consist of appending 0 and then 1 to the previous numbers
    # This behaviour can be mimicked using a queue until the result is complete
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n):
        res = [0]
        
        from collections import deque
        queue = deque()
        queue.append(1)

        while len(res) < n:
            cur = queue.popleft()
            
            res.append(cur)

            queue.append(cur)
            queue.append(cur + 1)
        return res
    
    # Dynamic Programming (Offset)
    # A similar approach can be done using dynamic programming
    # The offset corresponds to powers of 2 accordingly
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp 

    # Dynamic Programming (Bit Manipulation)
    # We can further improve the dp approach using bit manipulation
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n):
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp 