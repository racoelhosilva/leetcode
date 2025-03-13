"""
LeetCode Problem: Dota2 Senate
Problem Number: 649
Difficulty: Medium
Topic: Queue
Link: https://leetcode.com/problems/dota2-senate/
"""

from collections import deque

class Solution:
    # Two Queues
    # Keep a separate queue for each party
    # At each step, the lowest element in front of the queues will ban the other
    # Repeat until one of the queues is empty
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def predictPartyVictory(self, senate):
        radiants = deque()
        dires = deque()
        n = len(senate)
        for senator in range(n):
            if senate[senator] == 'R':
                radiants.append(senator)
            else:
                dires.append(senator)
        
        while radiants and dires:
            if radiants[0] < dires[0]:
                radiants.append(radiants[0] + n)
            else:
                dires.append(dires[0] + n)
            radiants.popleft()
            dires.popleft()
        return "Radiant" if radiants else "Dire"
