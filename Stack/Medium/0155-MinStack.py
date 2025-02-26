"""
LeetCode Problem: Min Stack
Problem Number: 155
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/min-stack/
"""

# Two Stack Approach
# Use one stack to store all the elements
# Use one stack to store the successive min elements
# Space Complexity: O(n)
class MinStack:

    # Initialize the stacks
    def __init__(self):
        self.main = []
        self.aux = []        

    # Add an element to the stack
    # Time Complexity: O(1)
    def push(self, val):
        self.main.append(val)
        if not self.aux or val <= self.aux[-1]:
            self.aux.append(val)

    # Remove an element from the stack
    # Time Complexity: O(1)
    def pop(self):
        elem = self.main.pop()
        if elem == self.aux[-1]:
            self.aux.pop()

    # Check last element of the stack
    # Time Complexity: O(1)
    def top(self):
        return self.main[-1]

    # Check min element of the stack
    # Time Complexity: O(1)
    def getMin(self):
        return self.aux[-1]

# One Stack Approach
# Use one stack to store all the elements, compared to the minimum one
# Perform necessary additions and subtractions for each operation
# Space Complexity: O(n)
class MinStack:

    # Initialize the stack and min
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    # Add an element to the stack
    # Time Complexity: O(1)
    def push(self, val):
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    # Remove an element from the stack
    # Time Complexity: O(1)
    def pop(self):
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val

    # Check last element of the stack
    # Time Complexity: O(1)
    def top(self):
        val = self.stack[-1]
        if val > 0:
            return val + self.min
        else:
            return self.min

    # Check min element of the stack
    # Time Complexity: O(1)
    def getMin(self):
        return self.min
