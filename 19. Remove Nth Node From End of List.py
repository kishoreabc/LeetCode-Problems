# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        curr = head
        length = 0
        while curr:
            temp.append(curr)
            length+=1
            curr = curr.next
        if length>n:
            temp[-n-1].next = temp[-n].next
        else:
            return temp[-n].next

        return head
        
