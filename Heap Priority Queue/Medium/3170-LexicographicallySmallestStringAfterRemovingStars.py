"""
LeetCode Problem: Lexicographically Smallest String After Removing Stars
Problem Number: 3170
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/lexicographically-smallest-string-after-removing-stars/
"""

class Solution:
    # Heap + Set
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def clearStars(self, s):
        import heapq
        smallest = []
        deleted = set()
        for idx in range(len(s)):
            if s[idx] == '*':
                _, i = heapq.heappop(smallest)
                deleted.add(-i)
                deleted.add(idx)
            else:
                heapq.heappush(smallest, (s[idx], -idx))
        return ''.join([s[idx] for idx in range(len(s)) if idx not in deleted])
    
    # Frequency array + Heap
    # Time Complexity: O(n) -> average; O(n log n) -> worst
    # Space Complexity: O(n)
    def clearStars(self, s):
        import heapq
        orda = ord('a')

        s = list(s)
        smallest = []
        freqs = [[] for _ in range(26)]
        
        for idx in range(len(s)):
            if s[idx] == '*':
                c = smallest[0]
                i = ord(c) - orda
                char_idx = freqs[i].pop()
                s[char_idx] = '*'
                if not freqs[i]:
                    heapq.heappop(smallest)
            else:
                i = ord(s[idx]) - orda
                if not freqs[i]:
                    heapq.heappush(smallest, s[idx])
                freqs[i].append(idx)
        return ''.join([char for char in s if char != '*'])
