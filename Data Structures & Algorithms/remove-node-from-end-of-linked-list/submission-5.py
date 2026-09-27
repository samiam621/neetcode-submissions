# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #go through the linked list
        #if is at nth position, remove the element

        if head is None:
            return None

        #get length of linked list
        curr1, length = head,0
        while curr1:
            curr1 = curr1.next
            length += 1

        if length-n == 0:
            head = head.next
            return head

        prev,curr,pos = None,head,0
        while curr:
            #point that prev node to the node after n
            #index = length - n
            if pos == length-n:
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next

            pos += 1

        return head