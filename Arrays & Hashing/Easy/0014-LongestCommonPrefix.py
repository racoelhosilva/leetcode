"""
LeetCode Problem: Longest Common Prefix
Problem Number: 14
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    # Horizontal Scanning
    # Time Complexity: O(n * l)
    # where n is the number of strings and l the length of the shortest
    # Space Complexity: O(1)
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        lcp = strs[0]
        for string in strs[1:]:
            for idx in range(len(lcp)):
                if idx >= len(string) or lcp[idx] != string[idx]:
                    lcp = string[0:idx]
                    break
            if lcp == "":
                return ""
        return lcp
    
    # Vertical Scanning
    # Although worst case complexity is the same, on average this solution is better
    # Time Complexity: O(n * l)
    # where n is the number of strings and l the length of the shortest
    # Space Complexity: O(1)
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for idx in range(len(strs[0])):
            for string in strs[1:]:
                if idx >= len(string) or strs[0][idx] != string[idx]:
                    return string[0:idx]
        return strs[0]
    
    # Trie Data Structure
    # By using a trie to store the strings, we can answer subsequent queries faster
    # Making the process of finding the lcp faster (after the construction step)
    # Nonetheless, it is overkill for this problem and worse for single queries 
    # Time Complexity: O(n * l)
    # where n is the number of strings and l its length
    # Space Complexity: O(t)
    # where t is the number of nodes
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        trie = Trie()
        for string in strs:
            trie.insert(string)
        return trie.longestCommonPrefix()

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = dict()
            self.end = False
    
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.end = True
    
    # Longest Common Prefix
    # Given a trie, finding the lcp is faster than the other approaches
    # Time Complexity: O(l)
    # Space Complexity: O(l)
    # where l is the length of the longest common prefix
    def longestCommonPrefix(self):
        string = ""
        node = self.root
        while not node.end and len(node.children) == 1:
            string += node.children.keys()[0]
            node = node.children.values()[0]
        return string
