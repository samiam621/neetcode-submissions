# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        queue = deque([(root,float('-inf'),float('inf'))])

        while queue:
            curr, low, high = queue.popleft() #a tuple

            l,r = curr.left,curr.right

            if (low < curr.val and curr.val < high):
                if l:
                    queue.append((l, low, curr.val))
                if r:
                    queue.append((r, curr.val, high))
            else:
                return False
                
        return True
            

            
