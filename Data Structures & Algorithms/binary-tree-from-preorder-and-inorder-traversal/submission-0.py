# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        
        root_val = preorder[0]
        root_ind = inorder.index(root_val)

        root = TreeNode(root_val)
        left_subtree_inorder = inorder[ : root_ind]
        right_subtree_inorder = inorder[root_ind + 1 : ]
        left_subtree_preorder = preorder[1 : root_ind + 1]
        right_subtree_preorder = preorder[root_ind + 1 : ]

        root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)

        return root