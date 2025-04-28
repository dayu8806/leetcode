# https://leetcode.com/problems/path-sum/description/?envType=problem-list-v2&envId=binary-tree

# 問題敘述
# 判斷一棵二叉樹中，是否存在一條由「根節點→葉節點」的路徑，使得這條路徑上所有節點的值相加後，等於給定的目標值。若有，回傳 true，否則回傳 false。

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum