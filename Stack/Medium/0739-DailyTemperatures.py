"""
LeetCode Problem: Daily Temperatures
Problem Number: 739
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/daily-temperatures/
"""

class Solution:
    # Monotonic Stack
    # At each step, if there are still unsolved values smaller than the current
    # Solve them using the current element
    # Otherwise, just mark the current element as unsolved
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev = stack.pop()
                res[prev] = idx - prev
            stack.append(idx)
        return res

    # Dynamic Programming
    # Although not the "intended" solution, we can traverse the list in reverse
    # For the current element, try to find the first largest element based on previous solutions
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n

        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            
            if j < n:
                res[i] = j - i
        return res
