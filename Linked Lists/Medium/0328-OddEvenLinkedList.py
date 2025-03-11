"""
LeetCode Problem: Odd Even Linked List
Problem Number: 328
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Odd and Even Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        temp = even = head.next

        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = temp
        return head
