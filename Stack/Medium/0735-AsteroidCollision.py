"""
LeetCode Problem: Asteroid Collision
Problem Number: 735
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/asteroid-collision/
"""

class Solution:
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def asteroidCollision(self, asteroids):
        from collections import deque
        stack = deque()

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return list(stack)
