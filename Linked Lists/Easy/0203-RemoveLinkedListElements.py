"""
LeetCode Problem: Remove Linked List Elements
Problem Number: 203
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Dummy Node, Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeElements(self, head, val):
        dummy = ListNode(-1, head)
        
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next
        
    # Dummy Node, One Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeElements(self, head, val):
        dummy = ListNode(-1, head)
        
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
