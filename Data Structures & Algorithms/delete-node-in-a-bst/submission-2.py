# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left and root.right):
                return root.left or root.right
            else:
                m = self.minNode(root.right)
                root.val = m.val
                root.right = self.deleteNode(root.right, m.val)
        return root