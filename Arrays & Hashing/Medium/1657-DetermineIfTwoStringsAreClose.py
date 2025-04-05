"""
LeetCode Problem: Determine if Two Strings Are Close
Problem Number: 1657
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
"""

class Solution:
    # Hash set (characters) + Hash map (frequencies)
    # Time COmplexity: O(n)
    # Space Complexity: O(1)
    def closeStrings(self, word1, word2):
        chars1, chars2 = set(), set()
        freqs1, freqs2 = dict(), dict()

        for char in word1:
            chars1.add(char)
            freqs1[char] = freqs1.get(char, 0) + 1

        for char in word2:
            chars2.add(char)
            freqs2[char] = freqs2.get(char, 0) + 1
        
        freqs1 = sorted(freqs1.values())
        freqs2 = sorted(freqs2.values())

        return chars1 == chars2 and freqs1 == freqs2

    # Optimization for 26 letters
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def closeStrings(self, word1, word2):
        freqs1 = [0] * 26
        freqs2 = [0] * 26

        for char in word1:
            freqs1[ord(char) - ord('a')] += 1

        for char in word2:
            letter = ord(char) - ord('a')
            if freqs1[letter] == 0:
                return False
            freqs2[letter] += 1
        
        for letter in range(26):
            if freqs1[letter] != 0 and freqs2[letter] == 0:
                return False

        freqs1 = sorted(freqs1)
        freqs2 = sorted(freqs2)

        for idx in range(26):
            if freqs1[idx] != freqs2[idx]:
                return False

        return True
    
    # Further Python optimizations
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def closeStrings(self, word1, word2):
        s1 = set(word1)
        s2 = set(word2)
        if s1 ^ s2:
            return False

        freqs1 = []
        freqs2 = []
        
        for char in s1:
            freqs1.append(word1.count(char))
            freqs2.append(word2.count(char))
        for num in freqs1:
            if num in freqs2:
                freqs2.remove(num)
            else:
                return False
        return True

