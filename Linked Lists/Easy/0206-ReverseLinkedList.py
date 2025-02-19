"""
LeetCode Problem: Reverse Linked List
Problem Number: 206
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 3 Pointer Approach
    # Keep a prev, cur and next pointers
    # At each stage, reverse the current node and update everything
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head):
        if not head:
            return None
        prev, cur, next = None, head, head.next
        while next:
            cur.next = prev
            prev = cur
            cur = next
            next = cur.next
        cur.next = prev
        return cur
