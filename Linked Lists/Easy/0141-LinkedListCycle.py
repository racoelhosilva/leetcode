"""
LeetCode Problem: Linked List Cycle
Problem Number: 141
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Floyd's Cycle Detection
    # Consider two pointers that initially start in the same position
    # At each step, slow pointer advances one element and fast advances two
    # If they meet, a cycle exists, otherwise, the fast reaches the end of the list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle(self, head):
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False