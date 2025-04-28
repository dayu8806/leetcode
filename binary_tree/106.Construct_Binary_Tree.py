# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=binary-tree

# 問題敘述
# 105: 從preorder-and-inorder來建立一個binary tree
# 106: 從inorder-and-postorder來建立一個binary tree

class Solution_105:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx + 1:])

                return root

        return build(preorder, inorder)


class Solution_106:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = deque(postorder)

        def build(postorder, inorder):
            if inorder:
                idx = inorder.index(postorder.pop())
                root = TreeNode(inorder[idx])

                root.right = build(postorder, inorder[idx + 1:])
                root.left = build(postorder, inorder[:idx])

                return root

        return build(postorder, inorder)