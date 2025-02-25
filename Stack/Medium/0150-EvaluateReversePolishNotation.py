"""
LeetCode Problem: Evaluate Reverse Polish Notation
Problem Number: 150
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

class Solution:
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(n1 - n2)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(int(float(n1)/ n2))
                case _:
                    stack.append(int(token))
        return stack.pop()
                
