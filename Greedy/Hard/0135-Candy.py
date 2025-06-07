"""
LeetCode Problem: Candy
Problem Number: 135
Difficulty: Hard
Topic: Greedy
Link: https://leetcode.com/problems/candy/
"""

class Solution:
    # Two Pass + Array
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        return sum(candies)

    # One Pass
    # First element will have 1 candy
    # From that point onwards: 
    # if the number of elements is equal to the previous one, then it gets one candy and everything is reset
    # if the number is larger than previous, we increase the amount given and add that amount
    # if the number is smaller than previous, we increase the amount given to the start of the downhill (peak)
    # Note that, if the downhill sequence is smaller than the previous peak, we don't need to increase the peak
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def candy(self, ratings):
        n = len(ratings)
        res = 1
        up = down = peak = 0
        
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                up += 1
                peak = up
                down = 0
                res += up + 1
            elif ratings[i-1] == ratings[i]:
                up = down = peak = 0
                res += 1
            else:
                up = 0
                down += 1
                res += down + (0 if peak >= down else 1)
        return res
