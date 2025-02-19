"""
LeetCode Problem: Middle of the Linked List
Problem Number: 876
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Floyd's Slow and Fast Pointer
    # Similarly to the cycle detection algorithm, the slow/fast pointers
    # can be used to find the middle of a linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def middleNode(self, head):
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow