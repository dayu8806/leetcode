#https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=problem-list-v2&envId=binary-tree

# 問題敘述
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if node is None:
                return 0

            gain_on_left = max(get_max_gain(node.left), 0)  # Read the part important observations
            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations

            current_max_path = node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
            max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

            return node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path