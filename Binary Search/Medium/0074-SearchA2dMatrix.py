"""
LeetCode Problem: Search a 2D Matrix
Problem Number: 74
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    # Staircase Search
    # Start from the top left corner and update row,col accordingly
    # Time Complexity: O(m + n)
    # Space Complexity: O(1)
    def searchMatrix(self, matrix, target):
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False

    # Binary Search (Row -> Column)
    # Perform binary search to find the row and then the element in the row
    # Time Complexity: O(log m + log n) = O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix(self, matrix, target):
        # Perform binary search to find the row that might contain the element
        # This can be done with a right-biased search, not overshooting up
        up, down = 0, len(matrix) - 1
        while up < down:
            mid = (up + down + 1) // 2
            if matrix[mid][0] > target:
                down = mid - 1
            else:
                up = mid
        row = matrix[up]

        # Perform binary search to find element in the row
        # The search has to be exact
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False
    
    # Binary Search (Row + Col)
    # Perform binary search on the entire matrix at once
    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m // COLS][m % COLS] < target:
                l = m + 1
            elif matrix[m // COLS][m % COLS] > target:
                r = m - 1
            else:
                return True
        return False
