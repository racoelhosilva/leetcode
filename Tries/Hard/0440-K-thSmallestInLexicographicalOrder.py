"""
LeetCode Problem: K-th Smallest in Lexicographical Order
Problem Number: 440
Difficulty: Hard
Topic: Tries
Link: https://leetcode.com/problems/kth-smallest-in-lexicographical-order/
"""

class Solution:
    # Skipping branches
    # At each step, we calculate the number of children from the current node
    # If this number is larger than k, we know that the k-th element is a child of the current node
    # which in this case means that the current number is a prefix
    # When this happens, we want to explore the children of the current number and so on until k = 0
    # If the step is smaller than k, we can skip directly to the next sibling of the current node
    # which in this case means adding 1 to the current number
    # When this happens, we are pruning/skipping all number that have that prefix
    # Time Complexity: O(log(n)^2)
    # Space Complexity: O(1)
    def findKthNumber(self, n, k):
        cur = 1
        k -= 1

        def children(n, parent):
            res = 0
            sibling = parent + 1
            while parent <= n:
                res += min(n + 1, sibling) - parent
                parent *= 10
                sibling *= 10
            return res

        while k > 0:
            step = children(n, cur)

            if step > k:
                cur *= 10
                k -= 1
            else:
                cur += 1
                k -= step

        return cur
