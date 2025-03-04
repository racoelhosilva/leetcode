"""
LeetCode Problem: Add Two Numbers
Problem Number: 2
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative Approach
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            cur.next = ListNode(total % 10)
            carry = total // 10
            cur = cur.next

        return dummy.next
