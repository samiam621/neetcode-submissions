# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        #search while theres still queued
        while queue:
            layerSize = len(queue)
            curr_layer = []

            for _ in range(layerSize):
                curr = queue.popleft() #grab the curr node
                #append the node on this layer
                curr_layer.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    
            res.append(curr_layer)
        
        return res


            


