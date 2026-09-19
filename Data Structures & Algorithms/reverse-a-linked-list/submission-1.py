# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack=[]
        node = head
        while node:
            stack.append(node)
            node=node.next
        
        new_head = stack.pop() #last stack, first/entry for reversed
        curr = new_head

        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return new_head

        
        



            