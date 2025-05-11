"""
LeetCode Problem: Car Fleet
Problem Number: 853
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/car-fleet/
"""

class Solution:
    # Sort + Monotonic Stack
    # One car will only catch the following car if the time it takes to reach target
    # is <= than the time of the following car (time = (target - position) / speed)
    # Having the times of all the cars, we can push them into a stack and keep monotonicity
    # by removing elements whose times are faster than the current one (they will form a fleet)
    # In the end, the stack will only have the fastests elements of each fleet
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        times = [float(target - position) / speed for position, speed in cars]
        stack = []
        for time in times:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)

    # Sort + Back Iteration
    # Having the times of all the cars, if we iterate from the front to the back
    # a new fleet is formed everytime a car takes longer than the current fleet
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        times = [float(target - position) / speed for position, speed in cars]
        res = cur = 0
        for time in times:
            if time > cur:
                res += 1
                cur = time
        return res
