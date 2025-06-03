"""
LeetCode Problem: Maximum Candies You Can Get from Boxes
Problem Number: 1298
Difficulty: Hard
Topic: Graphs
Link: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
"""

from collections import deque

class Solution:
    # Editorial-like BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        def is_open(box):
            return status[box] == 1
        
        n = len(status)
        seen = [False] * n
        used = [False] * n
        queue = deque()
        res = 0

        for box in initialBoxes:
            seen[box] = True
            if is_open(box):
                queue.append(box)
                used[box] = True

        while queue:
            box = queue.popleft()
            res += candies[box]

            for key in keys[box]:
                status[key] = 1
                if seen[key] and not used[key]:
                    queue.append(key)
                    used[key] = True
            
            for box in containedBoxes[box]:
                seen[box] = True
                if is_open(box) and not used[box]:
                    queue.append(box)
                    used[box] = True
        
        return res
    
    # Improved BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        res = 0
        update = True
        boxes = deque(initialBoxes)
        while boxes and update:
            update = False
            for _ in range(len(boxes)):
                box = boxes.popleft()
                if status[box]:
                    update = True
                    boxes.extend(containedBoxes[box])
                    for key in keys[box]:
                        status[key] = 1
                    res += candies[box]
                else:
                    boxes.append(box)
        return res
