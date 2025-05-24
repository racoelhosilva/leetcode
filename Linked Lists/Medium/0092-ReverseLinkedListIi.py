"""
LeetCode Problem: Reverse Linked List II
Problem Number: 92
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/reverse-linked-list-ii/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Fixed before and start elements
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(-1, head)

        before = dummy
        for _ in range(left - 1):
            before = before.next
        
        start = before.next
        for _ in range(right - left):
            cur = start.next
            start.next = cur.next
            cur.next = before.next
            before.next = cur

        return dummy.next
