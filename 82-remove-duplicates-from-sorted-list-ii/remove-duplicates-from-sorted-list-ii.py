# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head is not None and head.next is not None:
            if head.val != head.next.val:
                prev = head
                head = head.next
            else:
                dupl = head.val
                while head is not None and head.val == dupl:
                    head = head.next
                prev.next = head
        
        return dummy.next
        
