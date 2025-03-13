"""
LeetCode Problem: Implement Stack using Queues
Problem Number: 225
Difficulty: Easy
Topic: Queue
Link: https://leetcode.com/problems/implement-stack-using-queues/
"""

from collections import deque

# Using Two Queues
# One queue will contain the LIFO order
# The other is used for pushes
# Space Complexity: O(n)
class MyStack(object):

    # Initializing the queues
    def __init__(self):
        self.main = deque()
        self.aux = deque()

    # Pushing an element
    # Time Complexity: O(n)
    def push(self, x):
        self.aux.append(x)
        while self.main:
            self.aux.append(self.main.popleft())
        
        self.main, self.aux = self.aux, self.main

    # Popping an element
    # Time Complexity: O(1)
    def pop(self):
        return self.main.popleft()

    # Viewing the last inserted element
    # Time Complexity: O(1)
    def top(self):
        return self.main[0]

    # Checking if there are elements
    # Time Complexity: O(1)
    def empty(self):
        return not self.main
    
# Using One Queue
# Since we know the number of elements in queue, no need for auxiliar queue
# Space Complexity: O(n)
class MyStack(object):

    # Initializing the queue
    def __init__(self):
        self.main = deque()

    # Pushing an element
    # Time Complexity: O(n)
    def push(self, x):
        self.main.append(x)
        for _ in range(len(self.main) - 1):
            self.main.append(self.main.popleft())

    # Popping an element
    # Time Complexity: O(1)
    def pop(self):
        return self.main.popleft()

    # Viewing the last inserted element
    # Time Complexity: O(1)
    def top(self):
        return self.main[0]

    # Checking if there are elements
    # Time Complexity: O(1)
    def empty(self):
        return not self.main

# Queue of queues
# Using queues of queues to represent element and rest of queue
# Similar to a Linked List
# Space Complexity: O(n)
class MyStack(object):

    # Initializing the queue
    def __init__(self):
        self.queue = None

    # Pushing an element
    # Time Complexity: O(1)
    def push(self, x):
        self.queue = deque([x, self.queue])

    # Popping an element
    # Time Complexity: O(1)
    def pop(self):
        top = self.queue.popleft()
        self.queue = self.queue.popleft()
        return top

    # Viewing the last inserted element
    # Time Complexity: O(1)
    def top(self):
        return self.queue[0]
    
    # Checking if there are elements
    # Time Complexity: O(1)
    def empty(self):
        return not self.queue
