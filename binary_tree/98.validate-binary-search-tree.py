# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree

# 問題敘述
# 確定所給定的二元樹是否是嚴謹且符合規定的

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            # 基本情況：如果當前節點為 None，返回 True（空樹是有效的）
            if not node:
                return True

            val = node.val
            # 檢查當前節點是否在有效範圍內
            if val <= lower or val >= upper:
                return False

            # 遞迴處理左子樹和右子樹，並更新範圍
            return (helper(node.left, lower, val) and helper(node.right, val, upper))

        return helper(root)