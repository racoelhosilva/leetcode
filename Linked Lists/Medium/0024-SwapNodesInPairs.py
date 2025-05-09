"""
LeetCode Problem: Swap Nodes in Pairs
Problem Number: 24
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Dummy + Iterative Swapping
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def swapPairs(self, head):
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next:
            one, two, three = cur.next, cur.next.next, cur.next.next
            cur.next = two
            two.next = one
            one.next = three
            cur = one

        return dummy.next
