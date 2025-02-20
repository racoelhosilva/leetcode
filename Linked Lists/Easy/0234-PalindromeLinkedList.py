"""
LeetCode Problem: Palindrome Linked List
Problem Number: 234
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Middle, Reverse, Compare
    # Find middle of linked list using Fast and Slow pointer
    # Reverse the second half of the list
    # Compare elements from head and tail to middle
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Find middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse from middle of list to end
        prev, cur = slow, slow.next
        prev.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Compare elements
        tail = prev
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        
        return True
