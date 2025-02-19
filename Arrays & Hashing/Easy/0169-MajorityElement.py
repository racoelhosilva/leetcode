"""
LeetCode Problem: Majority Element
Problem Number: 169
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/majority-element/
"""

class Solution:
    # Middle Element after Sorting
    # After sorting, since the element appears more than half the length,
    # it will be middle element of the array
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[len(nums)//2]

    # One-Pass Hash Table Approach
    # While computing the frequencies of each element we can 
    # keep track the element with the highest frequency
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def majorityElement(self, nums):
        freq = dict()
        res = nums[0]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > freq[res]:
                res = num
        return res

    # Boyer-Moore Majority Voting Algorithm
    # To obtain the majority element we can keep track of a "chance"
    # of a certain candidate and update that chance accordingly
    # When it seems unlikely for the element to be correct, switch it
    # Since it appears over half the times, the end result will be correct
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums):
        candidate = nums[0]
        chance = 0
        for num in nums:
            if chance == 0:
                candidate = num
            if num == candidate:
                chance += 1
            else:
                chance -= 1
        return candidate
