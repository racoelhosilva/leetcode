"""
LeetCode Problem: Alternating Groups II
Problem Number: 3208
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/alternating-groups-ii/
"""

class Solution:
    # Brute-Force
    # Time Complexity: O(n * k) -> Time Limit Exceeded
    # Space Complexity: O(1)
    def numberOfAlternatingGroups(self, colors, k):
        res = 0
        n = len(colors)
        for l in range(n):
            check = True
            for r in range(l, l + k - 1):
                if (colors[r % n] == colors[(r+1) % n]):
                    check = False
                    break
            if check:
                res += 1
        return res    

    # Array Expansion + Sliding Window
    # Time Complexity: O(n + k)
    # Space Complexity: O(k)
    def numberOfAlternatingGroups(self, colors, k):
        for i in range(k-1):
            colors.append(colors[i])
        n = len(colors)
        res = 0
        l = r = 0
        
        while r < n:
            if colors[r-1] == colors[r]:
                l = r
            r += 1
            if (r - l) == k:
                res += 1
                l += 1

        return res

    # Last Color
    # Time Complexity: O(n + k)
    # Space Complexity: O(1)
    def numberOfAlternatingGroups(self, colors, k):
        res = 0
        last = colors[0]
        sequence = 0
        
        for idx in range(len(colors)):
            if colors[idx] == last:
                sequence = 0
            last = colors[idx]
            sequence += 1
            if sequence >= k:
                res += 1

        for idx in range(k-1):
            if colors[idx] == last:
                break
            last = colors[idx]
            sequence += 1
            if sequence >= k:
                res += 1

        return res
    
    # Last Color + Modulo Comparison
    # Time Complexity: O(n + k)
    # Space Complexity: O(1)
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        res = 0
        last = colors[0]
        sequence = 0
        
        for idx in range(len(colors) + k - 1):
            if colors[idx % n] == last:
                sequence = 0
            last = colors[idx % n]
            sequence += 1
            if sequence >= k:
                res += 1

        return res
