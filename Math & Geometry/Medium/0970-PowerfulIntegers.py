"""
LeetCode Problem: Powerful Integers
Problem Number: 970
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/powerful-integers/
"""

class Solution:
    # Pre-calculate all possible powers
    # Time Complexity: O((log x bound) * (log y bound))
    # Space Complexity: O((log x bound) * (log y bound))
    def powerfulIntegers(self, x, y, bound):
        xs = [1]
        num = x
        while num <= bound and num > 1:
            xs.append(num)
            num *= x
        ys = [1]
        num = y
        while num <= bound and num > 1:
            ys.append(num)
            num *= y
        
        res = set()
        for xc in xs:
            for yc in ys:
                num = xc + yc
                if num <= bound:
                    res.add(num)
                else:
                    break
        return list(res)
    
    # Set bounds for each of the variables
    # Time Complexity: O((log x bound) * (log y bound))
    # Space Complexity: O((log x bound) * (log y bound))
    def powerfulIntegers(self, x, y, bound):
        if bound == 0:
            return []
            
        import math
        xb = 1 if x == 1 else int(math.log(bound, x))
        yb = 1 if y == 1 else int(math.log(bound, y))

        res = set()
        for i in range(xb+1):
            for j in range(yb+1):
                val = x ** i + y ** j
                if val <= bound:
                    res.add(val)
        return list(res)
    