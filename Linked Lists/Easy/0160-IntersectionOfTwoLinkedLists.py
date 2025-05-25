"""
LeetCode Problem: Intersection of Two Linked Lists
Problem Number: 160
Difficulty: Easy
Topic: Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Hash Set
    # Time Complexity: O(n + m)
    # Space Complexity: O(n)
    def getIntersectionNode(self, headA, headB):
        nodes = set()
        cur = headA
        while cur:
            nodes.add(cur)
            cur = cur.next
        
        cur = headB
        while cur:
            if cur in nodes:
                return cur
            cur = cur.next
        return None
    
    # Length Difference
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0
        curA, curB = headA, headB
        while curA or curB:
            if curA:
                lenA += 1
                curA = curA.next
            if curB:
                lenB += 1
                curB = curB.next

        if lenA >= lenB:
            curA, curB = headA, headB
        else:
            curA, curB = headB, headA 
            lenA, lenB = lenB, lenA
        
        while lenA - lenB:
            lenA -= 1
            curA = curA.next

        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA

    # Swap Iteration
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            if curB:
                curB = curB.next
            else:
                curB = headA
        return curA
