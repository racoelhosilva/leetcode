"""
LeetCode Problem: Find Minimum Time to Reach Last Room I
Problem Number: 3341
Difficulty: Medium
Topic: Graphs Advanced
Link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
"""

class Solution:
    # Dijkstra's Algorithm
    # Time Complexity: O(mn log mn)
    # Space Complexity: O(mn)
    def minTimeToReach(self, moveTime):
        from heapq import heappop, heappush

        ROWS, COLS = len(moveTime), len(moveTime[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        dist = [[float("inf")] * COLS for _ in range(ROWS)]
        dist[0][0] = 0
        heap = [(0,0,0)] # Time, Row, Col

        while heap:
            time, row, col = heappop(heap)
            
            if (row, col) == (ROWS-1, COLS-1):
                return time
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    new_time = max(moveTime[nr][nc], time) + 1
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heappush(heap, (new_time, nr, nc))
        
        return -1
