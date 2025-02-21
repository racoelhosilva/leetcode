"""
LeetCode Problem: Implement Trie Prefix Tree
Problem Number: 208
Difficulty: Medium
Topic: Tries
Link: https://leetcode.com/problems/implement-trie-prefix-tree/
"""

# Explicit Node Implementation
# Another solution could store the tree in a single dict 
# and use, for example, '#' to mark end nodes
# Time Complexity: O(n)
# Space Complexity: O(t)
# where t is the number of nodes
class Trie:
    # Hash Map Node
    # If we consider only lowercase english characters, we can use an array
    class TrieNode:
        def __init__(self):
            self.children = dict()
            self.end = False
    
    # Initialize the root node
    def __init__(self):
        self.root = self.TrieNode()

    # Insert a word into the trie
    # While there is a match, traverse
    # Else create the nodes
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.end = True

    # Search a word in the trie
    # While there is a match, traverse
    # In the end, check if node is marked as end
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    # Check prefix of word in trie
    # While there is match, traverse
    # If there are still nodes, return True
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
