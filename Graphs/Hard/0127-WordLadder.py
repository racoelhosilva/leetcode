"""
LeetCode Problem: Word Ladder
Problem Number: 127
Difficulty: Hard
Topic: Graphs
Link: https://leetcode.com/problems/word-ladder/
"""

class Solution:
    # Generate Graph + BFS
    # Time Complexity: O(m * n^2)
    # Space Complexity: O(n^2)
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        # Generate Graph
        from collections import defaultdict
        adjacent = defaultdict(list)

        word_length = len(beginWord)
        dict_length = len(wordList)

        def similar(a, b):
            flag = False
            for idx in range(word_length):
                if a[idx] == b[idx]:
                    continue
                elif not flag:
                    flag = True
                else:
                    return False
            return True

        if beginWord not in wordList:
            for i in range(dict_length):
                if similar(beginWord, wordList[i]):
                    adjacent[wordList[i]].append(beginWord)
                    adjacent[beginWord].append(wordList[i])

        for i in range(dict_length):
            for j in range(i+1, dict_length):
                if i != j and similar(wordList[i], wordList[j]):
                    adjacent[wordList[i]].append(wordList[j])
                    adjacent[wordList[j]].append(wordList[i])

        # Traverse Graph (BFS)
        from collections import deque
        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        res = 1

        while queue:
            res += 1
            for a in range(len(queue)):
                word = queue.popleft()
                for adj in adjacent[word]:
                    if adj not in visited:
                        if adj == endWord:
                            return res
                        queue.append(adj)
                        visited.add(adj)
        
        return 0
    
    # BFS without generating graph 
    # Time Complexity: O(m^2 * n)
    # Space Complexity: O(m^2 * n)
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        from collections import deque

        m = len(beginWord)
        words = set(wordList)
        res = 0
        queue = deque()
        queue.append(beginWord)

        while queue:
            res += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for idx in range(m):
                    for char in range(ord('a'), ord('z')+1):
                        adj = word[:idx] + chr(char) + word[idx+1:]
                        if adj in words:
                            queue.append(adj)
                            words.remove(adj)
        
        return 0

    # Bidirectional Search BFS 
    # Time Complexity: O(m^2 * n)
    # Space Complexity: O(m^2 * n)
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        from collections import deque
        m = len(wordList[0])
        wordSet = set(wordList)
        beginQueue = deque([beginWord])
        endQueue = deque([endWord])
        beginVisited = set([beginWord])
        endVisited = set([endWord])
        res = 1

        while beginQueue and endQueue:
            res += 1
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
                beginVisited, endVisited = endVisited, beginVisited
            for _ in range(len(beginQueue)):
                word = beginQueue.popleft()
                for idx in range(m):
                    for char in range(ord('a'), ord('z')+1):
                        if char == word[idx]:
                            continue
                        adj = word[:idx] + chr(char) + word[idx+1:]
                        if adj not in wordSet:
                            continue
                        if adj in endVisited:
                            return res
                        if adj not in beginVisited:
                            beginQueue.append(adj)
                            beginVisited.add(adj)
        return 0
