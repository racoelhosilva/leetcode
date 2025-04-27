"""
LeetCode Problem: Maximum Twin Sum of a Linked List
Problem Number: 2130
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse from middle and compare
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pairSum(self, head):
        res = 0

        # Middle of the List
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse from middle to end
        cur = slow
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        # Compare pairs
        while prev:
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        return res
