# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, level = deque(), 0
        q.append(root)
        res = []
        while len(q):
            res.append([])
            for _ in range(len(q)):
                el = q.popleft()
                res[level].append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            level += 1
        
        return res