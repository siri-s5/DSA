# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def samet(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val!=n2.val:
                return False
            t1=samet(n1.left,n2.right)
            t2=samet(n1.right,n2.left)
            if t1 and t2:
                return True
            else:
                return False
        return samet(root.left,root.right) 