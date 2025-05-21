# https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20

# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].
#
# For each queries[i]:
#
# Select a subset of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.
#
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.


# O(n * q) time, too slow
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for i in range(len(queries)):
            for j in range(queries[i][0], queries[i][1] + 1):
                if nums[j] > 0:
                    nums[j] = nums[j] - 1

        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        return True


# Use a difference array to compute coverage in O(n + q) time
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for li, ri in queries:
            diff[li] -= 1
            if ri + 1 < n:
                diff[ri + 1] += 1
        sum_val = 0
        for i in range(n):
            sum_val += diff[i]
            if nums[i] > -sum_val:
                return False
        return True

# difference array（差分陣列）是一個非常常見又高效的技巧，常出現在區間更新問題或是陣列快速修改與查詢的演算法中。 可加快時間複雜度，節省 for loop 運算！！！
# 用來快速對一段區間的值做修改，差分陣列可以 O(1) 次數內完成修改
# 差分陣列 D 定義為： D[i] = A[i] - A[i - 1]  也就是說，第 i 位的差分，就是這個位置與前一個位置的差異。
# 例子：
# 原始 A = [5, 5, 5, 5, 5]
# D = [5, 0, 0, 0, 0]
# 對區間 [1, 3] 都 +2： D[1] += 2, D[4] -= 2
# D 現在變成：
# D = [5, 2, 0, 0, -2]
# 還原陣列，前綴加總
# A[0] = D[0]
# for i in range(1, n):
#     A[i] = A[i-1] + D[i]
