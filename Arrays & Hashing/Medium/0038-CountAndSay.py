"""
LeetCode Problem: Count and Say
Problem Number: 38
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/count-and-say/
"""

# Run Length Encoding
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
class Solution:
    def countAndSay(self, n):
        string = "1"
        for _ in range(1, n):
            temp = ""
            prev = string[0]
            count = 1
            for idx in range(1, len(string)):
                if prev == string[idx]:
                    count += 1
                else:
                    temp += str(count) + prev
                    prev = string[idx]
                    count = 1
            temp += str(count) + prev
            string = temp            
            
        return string
