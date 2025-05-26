"""
LeetCode Problem: Linked List Cycle II
Problem Number: 142
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Floyd's Fast Slow Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
