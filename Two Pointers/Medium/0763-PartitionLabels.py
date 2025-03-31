"""
LeetCode Problem: Partition Labels
Problem Number: 763
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/partition-labels/
"""

class Solution:
    # Two Pass Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(k) -> O(26) -> O(1) 
    def partitionLabels(self, s):
        last_index = dict()
        
        for i in range(len(s)):
            last_index[s[i]] = i
        
        end = 0
        start = 0
        res = []
        for i in range(len(s)):
            end = max(end, last_index[s[i]])
            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res