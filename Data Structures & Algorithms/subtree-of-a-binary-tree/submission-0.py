# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        else:
            result = self.isSameTree(root,subRoot)
            if result:
                return True
       
            return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

    def isSameTree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.right,subRoot.right) and self.isSameTree(root.left,subRoot.left)

                
                
            