# https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=math

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        tmp = [1, 1] + [0] * (n - 1)

        if n == 0 or n == 1:
            return tmp[n]

        for i in range(2, n + 1):
            for j in range(i):
                tmp[i] += tmp[j] * tmp[i - j - 1]

        return tmp[-1]