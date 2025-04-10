"""
LeetCode Problem: Delete the Middle Node of a Linked List
Problem Number: 2095
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Slow and Fast pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteMiddle(self, head):
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
