"""
LeetCode Problem: Copy List with Random Pointer
Problem Number: 138
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Hash Table (Two Pass)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def copyRandomList(self, head):
        copy_map = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            copy_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copy_map[cur]
            copy.next = copy_map[cur.next] 
            copy.random = copy_map[cur.random]
            cur = cur.next
        
        return copy_map[head]
    
    # Hash Table (One Pass)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def copyRandomList(self, head):
        copy_map = {None: None}
        
        cur = head
        while cur:
            if cur not in copy_map:
                copy_map[cur] = Node(cur.val)
            
            if cur.next not in copy_map:
                copy_map[cur.next] = Node(cur.next.val)
            copy_map[cur].next = copy_map[cur.next]

            if cur.random not in copy_map:
                copy_map[cur.random] = Node(cur.random.val)
            copy_map[cur].next = copy_map[cur.next]
            
            cur = cur.next
        
        return copy_map[head]
    
    # Node Interweaving (Space Optimization)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Create copies of nodes
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next
        
        res = head.next

        # Set the random nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Remove references
        cur = head
        while cur:
            new_node = cur.next
            cur.next = cur.next.next
            if new_node.next:
                new_node.next = new_node.next.next
            cur = cur.next
        
        return res
