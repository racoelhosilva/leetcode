"""
LeetCode Problem: Rotate List
Problem Number: 61
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/rotate-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Length + Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        size = 1
        end = head
        while end.next:
            end = end.next
            size += 1

        k = k % size
        if k == 0:
            return head

        end.next = head
        start = head
        for _ in range(size - k):
            start = start.next
        
        tmp = start
        start = start.next
        tmp.next = None
        return start
