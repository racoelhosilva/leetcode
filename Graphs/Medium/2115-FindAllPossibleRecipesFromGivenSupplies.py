"""
LeetCode Problem: Find All Possible Recipes from Given Supplies
Problem Number: 2115
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
"""

class Solution:
    # Breadth First Search
    # Time Complexity: O(r * i + s)
    # Space Complexity: O(r + s)
    def findAllRecipes(self, recipes, ingredients, supplies):
        from collections import deque
        
        supplies = set(supplies)
        queue = deque(range(len(recipes)))
        res = []
        last_iteration = -1

        while len(res) > last_iteration:
            last_iteration = len(res)

            for _ in range(len(queue)):
                recipe_idx = queue.popleft()

                if all(ingredient in supplies for ingredient in ingredients[recipe_idx]):
                    supplies.add(recipes[recipe_idx])
                    res.append(recipes[recipe_idx])
                else:
                    queue.append(recipe_idx)
        
        return res

    # Depth First Search
    # Time Complexity: O(r + i + s)
    # Space Complexity: O(r + i)
    def findAllRecipes(self, recipes, ingredients, supplies):
        supplies = set(supplies)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def dfs(recipe, visited):
            if recipe in supplies:
                return True
            
            if recipe in visited:
                return False

            if recipe not in recipe_to_idx:
                return False

            visited.add(recipe)

            if all(dfs(ingredient, visited) for ingredient in ingredients[recipe_to_idx[recipe]]):
                supplies.add(recipe)
                return True
            return False
        
        res = []
        for recipe in recipes:
            if dfs(recipe, set()):
                res.append(recipe)
        return res

    # Topological Sort
    # Time Complexity: O(r + i + s)
    # Space Complexity: O(r + i + s)
    def findAllRecipes(self, recipes, ingredients, supplies):
        from collections import defaultdict, deque
        
        supplies = set(supplies)
        recipe_to_idx = {recipe:idx for idx, recipe in enumerate(recipes)}
        requires = defaultdict(list)
        indegree = [0] * len(recipes)

        for idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in supplies:
                    requires[ingredient].append(recipes[idx])
                    indegree[idx] += 1
        
        queue = deque()
        for idx, ind in enumerate(indegree):
            if ind == 0:
                queue.append(idx)
        res = []

        while queue:
            idx = queue.popleft()
            res.append(recipes[idx])

            for required in requires[recipes[idx]]:
                indegree[recipe_to_idx[required]] -= 1
                if indegree[recipe_to_idx[required]] == 0:
                    queue.append(recipe_to_idx[required])

        return res
    
