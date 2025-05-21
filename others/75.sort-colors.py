# https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=sorting

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in range(len(nums)):
            # value = count.get(key, default):
            # key：要查找的字典键。
            # default：可选参数，如果 key 不在字典里，就返回 default。
            # 如果不传 default，get 会返回 None。
            count[nums[i]] = count.get(nums[i], 0) + 1

        idx = 0

        for color in range(3):
            freq = count.get(color, 0)
            nums[idx: idx + freq] = [color] * freq
            idx += freq


