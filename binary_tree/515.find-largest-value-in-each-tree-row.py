# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# 用遞迴帶著「當前深度」去更新結果陣列：
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def find_max(node, depth):
            if not node:
                return

            # 第一次到達這層，就把 node.val 當初始最大值
            if depth == len(res):
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val) # 否則跟已記錄的最大值比較並更新

            find_max(node.left, depth + 1)
            find_max(node.right, depth + 1)

        find_max(root, 0)
        return res


# BFS（Queue 層序遍歷）
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:   # root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
        if not root:
            return []

        res = []                          #此时 res = []
        queue = deque([root])             # queue = [1]

        while queue:                      #因为 queue 里有元素
            level_max = float('-inf')
            # 當前層的節點數
            sz = len(queue)               # 本层节点数

            for _ in range(sz):               # 循環本層結點數的次數
                node = queue.popleft()
                # 更新這層的最大值
                if node.val > level_max:
                    level_max = node.val
                # 把下一層節點加入佇列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_max)

        return res