"""
LeetCode Problem: Letter Combinations of a Phone Number
Problem Number: 17
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    # Backtracking
    # Time Complexity: O(n * 4 ^ n)
    # Space Complexity: O(n * 4 ^ n)
    def letterCombinations(self, digits):
        correspondence = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = []
        n = len(digits)
        def backtrack(idx, cur):
            if idx >= n:
                res.append("".join(cur))
                return
            for char in correspondence[digits[idx]]:
                cur.append(char)
                backtrack(idx+1)
                cur.pop()
        if digits:
            backtrack(0, [])
        return res

    # Iterative Approach
    # Time Complexity: O(n * 4 ^ n)
    # Space Complexity: O(n * 4 ^ n)
    def letterCombinations(self, digits):
        if not digits:
            return []
        correspondence = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = [""]
        for digit in digits:
            temp = []
            for prev in res:
                for char in correspondence[digit]:
                    temp.append(prev + char)
            res = temp
        return res
