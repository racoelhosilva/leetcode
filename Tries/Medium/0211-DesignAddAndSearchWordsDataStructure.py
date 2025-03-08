"""
LeetCode Problem: Design Add and Search Words Data Structure
Problem Number: 211
Difficulty: Medium
Topic: Tries
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

# Trie Node Definition
class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.word = False
    
# Word Dictionary Structure
# Uses TrieNodes for representation
# Note: a similar structure could be made using hash maps as nodes
# Space Complexity: O(n)
class WordDictionary:
    # Initialize the word dictionary
    def __init__(self):
        self.root = TrieNode()

    # Add a word to dictionary
    # Time Complexity: O(n)
    def addWord(self, word):
        cur = self.root

        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = TrieNode()
            cur = cur.nodes[char]

        cur.word = True 

    # Searches word in dictionary
    # Time Complexity: O(n)
    def search(self, word):
        def dfs(idx, node):
            for i in range(idx, len(word)):                    
                if word[i] == ".":
                    for adjacent in node.nodes.values():
                        if dfs(i + 1, adjacent):
                            return True
                    return False
                if word[i] not in node.nodes:
                    return False
                node = node.nodes[word[i]]
            return node.word 
        
        return dfs(0, self.root)
