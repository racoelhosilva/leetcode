"""
LeetCode Problem: Merge Two Sorted Lists
Problem Number: 21
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Merge Sorted
    # Create a dummy node and keep track of the current pointer in both lists
    # Sequentially set the next node as the smallest of the nodes and advance
    # When one list has no more elements, set the next element as the other list
    # Time Complexity: O(m + n)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1, list2):
        dummy = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if not list1:
            current.next = list2
        else:
            current.next = list1
        
        return dummy.next