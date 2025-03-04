"""
LeetCode Problem: Find the Duplicate Number
Problem Number: 287
Difficulty: Medium
Topic: Linked Lists
Link: https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    # Floyd's Cycle Detection
    # The input consists of an array with n+1 elements, each ranging between 1..n (one is repeated at least once)
    # We can consider that, each number in the array can be used as an index in the same array
    # Repeating this, we will get cycles of numbers between 1..n
    # Note that, this cycle can start in 0 (indexing the first element) but it will never reach it again since 0 is not in 1..n
    # So, to find a cycle, we can initialize slow and fast pointers at 0 and use floyd's cycle detection algorithm, treating the 
    # array values as indexes, resembling a linked list
    # When the cycle is found, we just need to find the starting element of the cycle (the duplicated element)
    # This can be done by starting another pointer at 0, and moving both 1 step at a time
    # This can be mathematically proved to always work
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
