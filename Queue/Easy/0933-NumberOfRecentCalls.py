"""
LeetCode Problem: Number of Recent Calls
Problem Number: 933
Difficulty: Easy
Topic: Queue
Link: https://leetcode.com/problems/number-of-recent-calls/
"""

from collections import deque

# Queue
# Space Complexity: O(n)
class RecentCounter:

    # Initializing Queue
    def __init__(self):
        self.queue = deque()

    # Pinging the Queue
    # Time Complexity: O(1) -> Amortized
    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.popleft()
        return len(self.queue)
