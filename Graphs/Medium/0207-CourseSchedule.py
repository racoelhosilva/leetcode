"""
LeetCode Problem: Course Schedule
Problem Number: 207
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/course-schedule/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict
        
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if not pre[course]:
                return True
            
            visiting.add(course)
            for prerequisite in pre[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            pre[course] = [] # Prevent repeated computations
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    # Topological Sort (Kahn's Algorithm)
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def canFinish(self, numCourses, prerequisites):
        from collections import deque
        
        indegree = [0] * numCourses
        pre = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            pre[course].append(prerequisite)
        
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        courses = 0
        while queue:
            course = queue.popleft()
            courses += 1
            for prerequisite in pre[course]:
                indegree[prerequisite] -= 1 
                if indegree[prerequisite] == 0:
                    queue.append(prerequisite)
        
        return courses == numCourses
