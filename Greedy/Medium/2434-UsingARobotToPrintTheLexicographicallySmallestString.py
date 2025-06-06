"""
LeetCode Problem: Using a Robot to Print the Lexicographically Smallest String
Problem Number: 2434
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
"""


class Solution:
    # Stack + Counter
    # Keep a counter of all the characters in the string
    # Initialize a minimum char tracker that starts with "a"
    # At each step, push the character into the stack and update the counter
    # If the character was the smallest remaining element, update minimum to next minimum char
    # While the top element of the stack is smaller than the smallest character yet to come, pop
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def robotWithString(self, s):
        from collections import Counter
        cnt = Counter(s)
        stack = []
        res = []
        min_char = "a"

        for char in s:
            stack.append(char)
            cnt[char] -= 1
            while min_char != "z" and cnt[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            while stack and stack[-1] <= min_char:
                res.append(stack.pop())
        return "".join(res)

    # Stack + Min Suffix Array
    # Pre-compute for each index the smallest character from that index to the end of the string
    # Iterate through the string and for each character append to the stack (robot)
    # While the smallest character yet to come is larger than the current top of the stack, pop
    # In the end, append the reverse of the rest of the stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def robotWithString(self, s):
        n = len(s)
        min_suffix = [s[-1]] * n
        stack = []
        res = []

        for i in range(n-2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i+1])

        for i, char in enumerate(s):
            stack.append(char)
            while stack and i < n - 1 and min_suffix[i + 1] >= stack[-1]:
                res.append(stack.pop())
        res.extend(stack[::-1])

        return "".join(res)
