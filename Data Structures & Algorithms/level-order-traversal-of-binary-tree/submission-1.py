# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        res = []
        level = 0
        q.append(root)
        while len(q):
            if len(res) == level:
                res.append([])
                for i in range(len(q)):
                    curr = q.popleft()
                    res[level].append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                level += 1
        
        return res