"""
LeetCode Problem: Merge k Sorted Lists
Problem Number: 23
Difficulty: Hard
Topic: Linked Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Merge K Sorted 
    # Time Complexity: O(n * k)
    # Space Complexity: O(1)
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        cur = dummy

        while cur:
            next_idx = -1
            for idx in range(len(lists)):
                if lists[idx] and (next_idx != -1 or lists[idx].val < lists[next_idx].val):
                    next_idx = idx
            
            if next_idx != -1:
                cur.next = lists[next_idx]
                lists[next_idx] = lists[next_idx].next
            else:
                cur.next = None
    
            cur = cur.next

        return dummy.next
    
    # Heap
    # Time Complexity: O(n log k)
    # Space Complexity: O(k) 
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        import heapq
        class NodeWrapper:
            def __init__(self, node=None):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        dummy = ListNode(-1)
        cur = dummy
        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, NodeWrapper(node))
        
        while heap:
            node = heapq.heappop(heap).node
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))

        return dummy.next
    
    # Divide and Conquer
    # Time Complexity: O(n log k)
    # Space Complexity: O(log k)
    def mergeKLists(self, lists):
        def divide(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            m = (l + r) // 2
            left = divide(lists, l, m)
            right = divide(lists, m + 1, r)
            return conquer(left, right)
        
        def conquer(l1, l2):
            dummy = ListNode(-1)
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return dummy.next

        if not lists or len(lists) == 0:
            return None
        return divide(lists, 0, len(lists) - 1)
