# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/?envType=problem-list-v2&envId=binary-tree

# 問題敘述
# 給定一個非空的二元樹，請返還搭第二小的值，如果只有最小的數值請返回-1

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        mn1 = mn2 = float('inf')

        def traverse(root):
            nonlocal mn1, mn2  # nonlocal是告訴函數我要對外部的參數進行操作，如果不加nonlocal只能讀取不能操作
            if not root:
                return
            if root.val < mn1:
                mn2, mn1 = mn1, root.val
            elif mn2 > root.val > mn1:
                mn2 = root.val

            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return mn2 if mn2 < float('inf') else -1