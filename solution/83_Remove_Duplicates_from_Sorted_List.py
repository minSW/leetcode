# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        now = head
        while now and now.next :
            if now.val == now.next.val :
                now.next = now.next.next
            else :
                now = now.next
        return head
