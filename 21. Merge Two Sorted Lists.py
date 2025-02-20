# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        while list1 or list2:
            l1= list1.val if list1 else float('inf')
            l2= list2.val if list2 else float('inf')
            if l1<l2:
                curr.next = ListNode(l1)
                list1 = list1.next
            else:
                curr.next = ListNode(l2)
                list2 = list2.next
            curr = curr.next
        return result.next
            
            

        
