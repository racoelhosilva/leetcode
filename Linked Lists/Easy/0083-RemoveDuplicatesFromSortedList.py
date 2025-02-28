"""
LeetCode Problem: Remove Duplicates from Sorted List
Problem Number: 83
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        prev, cur = head, head.next
        while cur:
            while cur and cur.val == prev.val:
                cur = cur.next
            prev.next = cur
            prev, cur = cur, cur.next

        return head
    
    # One Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
