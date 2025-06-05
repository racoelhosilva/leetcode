"""
LeetCode Problem: Last Substring in Lexicographical Order
Problem Number: 1163
Difficulty: Hard
Topic: Two Pointers
Link: https://leetcode.com/problems/last-substring-in-lexicographical-order/
"""

class Solution:
    # Two Pointer
    # The last substring in lexicographical order will always be a suffix of the word
    # Therefore, we need to find the start of the sequence
    # We will use two pointers, i will track the start and j will be used to check for other suffixes
    # In case s[i] == s[j], we might have a larger substring with the same preffix (we need to check)
    # In these cases, we increase the comparison offset until we know which solution is best:
    # If s[i+k] > s[j+k], i is the last one and we just have to update j
    # Otherwise, i should be updated to the largest between j and the next unverified character
    # In the last case, we must also update j
    # After solving the conflict, we must also set the offset to 0 again
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lastSubstring(self, s):
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            else:
                if s[i + k] > s[j + k]:
                    j += k + 1
                else:
                    i = max(i + k + 1, j)
                    j = i + 1
                k = 0
        return s[i:]
