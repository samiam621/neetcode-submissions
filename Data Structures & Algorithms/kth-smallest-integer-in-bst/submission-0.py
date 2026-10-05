# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #smallest index is the one that gets curr.next is None first 
        #dfs, while loop + stack for this problem. inorder traversal
        #return the kth smallest value in the tree so return node val
       stack = []
       curr = root
       while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        #at the furthest left node before no node
        curr = stack.pop()
        k -= 1
        if k==0:
            return curr.val
        #check right
        curr = curr.right
            




