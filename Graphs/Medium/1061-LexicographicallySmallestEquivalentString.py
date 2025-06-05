"""
LeetCode Problem: Lexicographically Smallest Equivalent String
Problem Number: 1061
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
"""

class Solution:
    # Union-Find Disjoin Set Solution (Hash map)
    # Note: a similiar solution could also be made with an array of size 26
    # Time Complexity: O(n + m)
    # Space Complexity: O(26) -> O(1)
    def smallestEquivalentString(self, s1, s2, baseStr):
        union_find = {}

        def find(x):
            if x not in union_find:
                union_find[x] = x
            if x != union_find[x]:
                union_find[x] = find(union_find[x])
            return union_find[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx <= ry:
                union_find[ry] = rx
            else:
                union_find[rx] = ry
        
        for idx in range(len(s1)):
            union(s1[idx], s2[idx])
        
        res = []
        for char in baseStr:
            res.append(find(char))
        
        return "".join(res)
