# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if root.val == key:
            if not (root.left and root.right):
                return root.left or root.right
        
            temp = root.right
            if not temp.left:
                temp.left = root.left
                return temp
            
            while temp.left.left:
                temp = temp.left
            temp.left.left = root.left
            temp.left.right = root.right
            root = temp.left
            temp.left = None
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        root.right = self.deleteNode(root.right, key)
        return root
        
        