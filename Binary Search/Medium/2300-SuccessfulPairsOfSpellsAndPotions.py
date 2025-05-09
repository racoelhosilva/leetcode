"""
LeetCode Problem: Successful Pairs of Spells and Potions
Problem Number: 2300
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"""

class Solution:
    # Binary Search
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(spells)
        m = len(potions)
        res = [0] * n

        def bs(spell):
            l, r = 0, m-1
            res = m
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * spell <= success:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        for i in range(n):
            res[i] = m - bs(spells[i])
        
        return res
    
    # Builtin Libraries
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def successfulPairs(self, spells, potions, success):
        from bisect import bisect_left

        potions.sort()
        n = len(spells)
        m = len(potions)
        res = [0] * n

        for i in range(n):
            spell = spells[i]
            min_potion = (success + spell - 1) // spell
            index = bisect_left(potions, min_potion)
            res[i] = m - index

        return res
