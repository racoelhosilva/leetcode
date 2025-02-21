"""
LeetCode Problem: Baseball Game
Problem Number: 682
Difficulty: Easy
Topic: Stack
Link: https://leetcode.com/problems/baseball-game/
"""

class Solution:
    # Stack 
    # Use a stack to keep track of the scores and perform operations
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def calPoints(self, operations):
        stack = []
        for op in operations:
            match op:
                case "C": 
                    stack.pop()
                case "D": 
                    stack.append(stack[len(stack)-1] * 2)
                case "+": 
                    stack.append(stack[len(stack)-2] + stack[len(stack)-1])
                case _:
                    stack.append(int(op))
        return sum(stack)
