"""
LeetCode Problem: Search Suggestions System
Problem Number: 1268
Difficulty: Medium
Topic: Tries
Link: https://leetcode.com/problems/search-suggestions-system/
"""

class Solution:
    # Sort + Binary Search
    # Time Complexity: O(n log n + m log n)
    # Space Complexity: O(m)
    def suggestedProducts(self, products, searchWord):
        from bisect import bisect_left

        products.sort()
        res = []
        prefix = ""
        idx = 0

        for char in searchWord:
            prefix += char
            idx = bisect_left(products, prefix, idx)
            cur = []
            for word_idx in range(idx, min(idx + 3, len(products))):
                if products[word_idx].startswith(prefix):
                    cur.append(products[word_idx])
            res.append(cur)
            
        return res

    # Sort + Two Pointers
    # Time Complexity: O(n log n + m)
    # Space Complexity: O(m)
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        l, r = 0, len(products) - 1

        for idx in range(len(searchWord)):
            char = searchWord[idx]
            while l <= r and (len(products[l]) <= idx or products[l][idx] != char):
                l += 1
            while l <= r and (len(products[r]) <= idx or products[r][idx] != char):
                r -= 1
            
            cur = []
            print(l, r)
            for word_idx in range(l, min(l + 3, r + 1)):
                cur.append(products[word_idx])
            res.append(cur)

        return res

    # Trie + DFS
    # Time Complexity: O(n * l + m)
    # Space Complexity: O(n * l)
    def suggestedProducts(self, products, searchWord):
        products.sort()
        root = TrieNode()

        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        res = []
        node = root
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])
        return res

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.suggestions = []
