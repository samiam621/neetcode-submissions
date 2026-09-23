# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l,r = head,head
        lst = [r] 

        while r and r.next is not None:
            r = r.next
            lst.append(r)
        
        #at each node, you point it to the tail 
        #two pointers
        l,r = 0, len(lst)-1

        order = []
        while l < r:
            
            order.append(lst[l])
            order.append(lst[r])
            
            l += 1
            r -= 1
        if l == r:
            order.append(lst[l])
   
     
        for i in range(1,len(order)):
            order[i-1].next=order[i]
        order[-1].next = None
