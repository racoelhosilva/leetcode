"""
LeetCode Problem: Binary Search
Problem Number: 704
Difficulty: Easy
Topic: Binary Search
Link: https://leetcode.com/problems/binary-search/
"""

class Solution:
    # Linear Search
    # Sequentially search for the target in the array until found
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, nums, target):
        for idx, num in enumerate(nums):
            if num == target:
                return idx
        return -1
    
    # Binary Search
    # Since the array is sorted, check the middle element and 
    # prune half of the search space in each iteration
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
    
    """ Notes about Binary Search:
    - In some languages, middle element might lead to overflow during calculation
        + Solutions: 
            mid = low + (high - low) // 2
            mid = (high + low) >> 1
    - Pruning can be done by upper or lower bound or without considering the mid element
    """

    # Python Bisect
    # Python has a library to implement this algorithm
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums, target):
        import bisect
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1