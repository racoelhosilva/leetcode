"""
LeetCode Problem: Online Stock Span
Problem Number: 901
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/online-stock-span/
"""

# Monotonic Stack
# Space Complexity: O(n)
class StockSpanner(object):

    # Initialize the stack
    def __init__(self):
        self.stack = []

    # Add a new stock price
    # Time Complexity: O(1) -> Amortized
    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span 
