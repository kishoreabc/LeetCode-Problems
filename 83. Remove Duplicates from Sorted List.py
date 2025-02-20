# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head.next
        last = head
        while curr:
            if curr.val != last.val:
                last.next = curr
                last = curr
            curr = curr.next
        last.next = None
        return head

