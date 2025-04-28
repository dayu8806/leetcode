# https://leetcode.com/problems/first-bad-version/description/

# 問題敘述
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


class Solution:
    def firstBadVersion(self, n: int) -> int:
        def find(low, high):
            if high - low == 1:
                return high

            mid = (high - low) // 2 + low
            if isBadVersion(mid):
                return find(low, mid)  # 因為想要傳遞值回來，所以需要添加return。如果只是想要修改變數不傳遞值則可以不用添加。
            else:
                return find(mid, high)

        return find(0, n)


# other answer with fast speed
class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n

        while first < last:
            mid = first + (last - first) // 2

            if isBadVersion(mid):
                last = mid  # The first bad version could be mid or before.
            else:
                first = mid + 1  # The first bad version must be after mid.

        return first  # At the end, first will be the first bad version.