"""
LeetCode Problem: Course Schedule II
Problem Number: 210
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/course-schedule-ii/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def findOrder(self, numCourses, prerequisites):
        from collections import defaultdict
        
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)
        
        visited, visiting = set(), set()
        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for prerequisite in pre[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order

    # Topological Sort (Kahn's Algorithm)
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def findOrder(self, numCourses, prerequisites):
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
        
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for prerequisite in pre[course]:
                indegree[prerequisite] -= 1
                if indegree[prerequisite] == 0:
                    queue.append(prerequisite)
            
        return order[::-1] if len(order) == numCourses else []

    # Topological Sort (DFS)
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def findOrder(self, numCourses, prerequisites):
        from collections import deque

        indegree = [0] * numCourses
        pre = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            pre[course].append(prerequisite)
        
        order = []

        def dfs(course):
            order.append(course)
            indegree[course] -= 1
            for prerequisite in pre[course]:
                indegree[prerequisite] -= 1
                if indegree[prerequisite] == 0:
                    dfs(prerequisite)


        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)
            
        return order[::-1] if len(order) == numCourses else []
