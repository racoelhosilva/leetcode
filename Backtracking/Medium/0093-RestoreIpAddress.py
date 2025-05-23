"""
LeetCode Problem: Restore IP Address
Problem Number: 93
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/restore-ip-address/
"""

class Solution:
    # Iterative Approach
    # Time Complexity: O(1)
    # Space Complexity: O(k)
    def restoreIpAddresses(self, s):
        def is_valid(segment):
            return segment == "0" or (segment[0] != "0" and 1 <= int(segment) <= 255)

        n = len(s)
        res = []
        
        for i in range(1, min(4, n - 2)):
            s1 = s[:i]
            if not is_valid(s1):
                continue

            for j in range(i + 1, i + min(4, n - i - 1)):
                s2 = s[i:j]
                if not is_valid(s2):
                    continue

                for k in range(j + 1, j + min(4, n - j)):
                    s3 = s[j:k]
                    s4 = s[k:]
                    
                    if 0 < len(s4) <= 3 and is_valid(s3) and is_valid(s4):
                        res.append(s1+'.'+s2+'.'+s3+'.'+s4)
                        
        return res

    # Backtracking Approach
    # Time Complexity: O(1)
    # Space Complexity: O(k)
    def restoreIpAddresses(self, s):
        res = []
        octets = []

        def backtrack(idx):
            if len(octets) == 4:
                if idx == len(s):
                    res.append('.'.join(octets))
                return

            for size in range(1, 4):
                if idx + size > len(s):
                    break

                octet = s[idx:idx+size]

                if (len(octet) > 1 and octet[0] == '0') or int(octet) > 255:
                    continue

                octets.append(octet)
                backtrack(idx + size)
                octets.pop()

        backtrack(0)
        return res
