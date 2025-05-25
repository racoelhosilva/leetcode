"""
LeetCode Problem: Flatten Nested List Iterator
Problem Number: 341
Difficulty: Medium
Topic: Queue
Link: https://leetcode.com/problems/flatten-nested-list-iterator/
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque

# Queue Approach
# Space Complexity: O(n)
class NestedIterator:

    # Initialize the queue
    def __init__(self, nestedList):
        self.queue = deque(nestedList)

    # Retrieve next element
    # Since hasNext will be called first, we can assume it as flattened
    # Time Complexity: O(1)
    def next(self):
        return self.queue.popleft().getInteger()
    
    # Check for next element
    # Time Complexity: O(1) -> Amortized
    def hasNext(self):
        while self.queue:
            if self.queue[0].isInteger():
                return True
            self.queue.extendleft(self.queue.popleft().getList()[::-1])
        return False

# Pre-calculation
# Space Complexity: O(n)
class NestedIterator:

    # Initialize the queue
    def __init__(self, nestedList):
        self.queue = deque()
        self.flatten(nestedList)

    # Retrieve next element
    # Time Complexity: O(1)
    def next(self):
        return self.queue.popleft()
    
    # Check for next element
    # Time Complexity: O(1)
    def hasNext(self):
        return len(self.queue) > 0
    
    # Pre-flatten the list using DFS
    # Time Complexity: O(n)
    def flatten(self, nestedList):
        for elem in nestedList:
            if elem.isInteger():
                self.queue.append(elem.getInteger())
            else:
                self.flatten(elem.getList())
