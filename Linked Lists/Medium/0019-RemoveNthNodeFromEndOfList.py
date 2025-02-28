"""
LeetCode Problem: Remove Nth Node From End of List
Problem Number: 19
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1, head)

        slow, fast = dummy, head
        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
