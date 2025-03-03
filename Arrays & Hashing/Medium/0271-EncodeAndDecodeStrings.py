"""
LeetCode Problem: Encode and Decode Strings
Problem Number: 271
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/encode-and-decode-strings/
"""

# Length Based Approach
# Time Complexity: O(n)
# Size Complexity: O(n)
class Solution:
    def encode(self, strs):
        res = ""
        for string in strs:
            res += len(string) + '#' + string
        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

# Flag Escape Approach
# Time Complexity: O(n)
# Size Complexity: O(n)
class Solution:
    def __init__(self):
        self.flag = "#"
        self.escape = "_"

    def encode(self, strs):
        res = []
        for string in strs:
            temp = []
            for char in string:
                if char == self.flag or char == self.escape:
                    temp.append(self.escape)
                temp.append(char)
            res.append("".join(temp))
        return "".join(res)

    def decode(self, s):
        res = []
        word = []
        escaped = False
        for char in s:
            if escaped:
                word.append(char)
                escaped = False
            elif char == self.escape:
                escaped = True
            elif char == self.flag:
                res.append("".join(word))
                word = []
            else:
                word.append(char)
        return res
