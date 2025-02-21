"""
LeetCode Problem: Lemonade Change
Problem Number: 860
Difficulty: Easy
Topic: Greedy
Link: https://leetcode.com/problems/lemonade-change/
"""

class Solution:
    # Greedy Approach
    # To give change, we need to keep track of 5s (for 10s and 20s) and 10s (for 20s)
    # 20s can be returned with either three 5s or one 5 and on 10
    # The greedy approach here is to always use the highest bills as much as possible
    # Since 10s are only used for 20s, give priority to them over 5s
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False   
            else:
                if ten >= 1 and five >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True