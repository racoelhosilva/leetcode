"""
LeetCode Problem: Reorder List
Problem Number: 143
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/reorder-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Middle, Reverse, Intersperse
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Middle of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse from middle to end
        cur = slow.next
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Intersperse
        start = cur = head
        end = prev
        while end:
            start = start.next
            cur.next = end
            cur = cur.next

            end = end.next
            cur.next = start
            cur = cur.next
