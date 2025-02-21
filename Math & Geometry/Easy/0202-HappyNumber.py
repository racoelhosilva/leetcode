"""
LeetCode Problem: Happy Number
Problem Number: 202
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/happy-number/
"""

class Solution:
    # Hash Set
    # Store visited numbers in a set to track loops
    # If number reaches one, return True
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def isHappy(self, n):
        def nextNumber(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        sequence = set()
        while n != 1:
            if n in sequence:
                return False
            sequence.add(n)
            n = nextNumber(n)
        return True

    # Floyd's Slow/Fast Pointer
    # Use two pointer approach to check for loops
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def isHappy(self, n):
        def nextNumber(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        slow, fast = n, nextNumber(n)
        while fast != 1:
            if slow == fast:
                return False
            slow = nextNumber(slow)
            fast = nextNumber(nextNumber(fast))
        return True
            