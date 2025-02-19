"""
LeetCode Problem: Implement Queue using Stacks
Problem Number: 232
Difficulty: Easy
Topic: Stack
Link: https://leetcode.com/problems/implement-queue-using-stacks/
"""

# Naive Implementation
# Keep a stack ordered like a queue
# Use auxiliar stack for moving values
# Space Complexity: O(n)
class MyQueue:
    def __init__(self):
        self.main = []
        self.aux = []

    # Time Complexity: O(n)
    def push(self, x):
        while self.main:
            self.aux.append(self.main.pop())
        self.main.append(x)
        while self.aux:
            self.main.append(self.aux.pop())

    # Time Complexity: O(1)
    def pop(self):
        return self.main.pop()

    # Time Complexity: O(1)
    def peek(self):
        return self.main[-1]

    # Time Complexity: O(1)
    def empty(self):
        return not self.main

# Amortized Implementation
# Keep an auxiliar stack for pushed values
# When popping or peeking, move values from auxiliar to main
# Main will keep all values ordered like a queue
# Space Complexity: O(n)
class MyQueue:
    def __init__(self):
        self.main = []
        self.aux = []

    # Time Complexity: O(1) 
    def push(self, x):
        if self.empty:
            self.main.append(x)
        else:
            self.aux.append(x)

    # Time Complexity: O(n)
    def move(self):
        while self.aux:
            self.main.append(self.aux.pop())

    # Time Complexity: O(1) -> Amortized
    # Move operation may not occur
    def pop(self):
        if not self.main:
            self.move()
        return self.main.pop()

    # Time Complexity: O(1) -> Amortized
    # Move operation may not occur
    def peek(self):
        if not self.main:
            self.move()
        return self.main[-1]

    # Time Complexity: O(1)
    def empty(self):
        return not self.main and not self.aux