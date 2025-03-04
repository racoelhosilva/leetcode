"""
LeetCode Problem: Valid Sudoku
Problem Number: 36
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/valid-sudoku/
"""

class Solution:
    # Brute Force (3 passes)
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def isValidSudoku(self, board):
        ROWS, COLS = len(board), len(board[0])
        
        # Row check
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        # Col check     
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        
        # Square check
        for R in range(0, ROWS, 3):
            for C in range(0, COLS, 3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[R * 3 + r][C * 3 + c] == ".":
                            continue
                        elif board[R * 3 + r][C * 3 + c] in seen:
                            return False
                        else:
                            seen.add(board[R * 3 + r][C * 3 + c])
        
        return True
    
    # Hash Set (1 pass)
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def isValidSudoku(self, board):
        ROWS, COLS = len(board), len(board[0])

        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqrs[(r // 3) * 3 + (c // 3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sqrs[(r // 3) * 3 + (c // 3)].add(board[r][c])
        
        return True
    
    # Bitmasks
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def isValidSudoku(self, board):
        ROWS, COLS = len(board), len(board[0])

        rows = [0] * 9
        cols = [0] * 9
        sqrs = [0] * 9

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                digit = int(board[r][c]) - 1
                if ((1 << digit) & rows[r]) or ((1 << digit) & cols[c]) or ((1 << digit) & sqrs[(r // 3) * 3 + (c // 3)]):
                    return False
                else:
                    rows[r] |= 1 << digit
                    cols[c] |= 1 << digit
                    sqrs[(r // 3) * 3 + (c // 3)] |= 1 << digit
        
        return True
