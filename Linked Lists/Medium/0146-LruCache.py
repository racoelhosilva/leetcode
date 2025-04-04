"""
LeetCode Problem: LRU Cache
Problem Number: 146
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/lru-cache/
"""

# Auxiliar representation of a Doubly Linked List node
class DLLNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

# Doubly Linked List + Hash Table of Key to Node
# Store the values as nodes in a doubly linked list and update them when needed
# Space Complexity: O(n)
class LRUCache:

    # Initialize the cache with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head, self.tail = DLLNode(-1, -1), DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Auxiliar function to insert a node at the end of the list (MRU)
    # Time Complexity: O(1)
    def __insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt

    # Auxiliar function to remove a node (either LRU or on update)
    # Time Complexity: O(1)
    def __remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Retrieve element from LRU Cache
    # If the element is present, it's position should be updated to MRU
    # Time Complexity: O(1)
    def get(self, key):
        if key in self.cache:
            self.__remove(self.cache[key])
            self.__insert(self.cache[key])
            return self.cache[key].val
        return -1

    # Add element to LRU Cache
    # If key already exists, remove that element
    # New element is added as MRU
    # If capacity is exceeded, remove the LRU element
    # Time Complexity: O(1)
    def put(self, key, value):
        if key in self.cache:
            self.__remove(self.cache[key])
        self.cache[key] = DLLNode(key, value)
        self.__insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.__remove(lru)
            del self.cache[lru.key]

from collections import OrderedDict

# Built-in Python OrderedDict
# Space Complexity: O(n)
class LRUCache:

    # Initialize the data structure
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # Retrieve item from LRU Cache
    # Time Complexity: O(1)
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    # Add item to the LRU Cache
    # Time Complexity: O(1)
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
