# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev_head = prev = ListNode(0, head)
        now = head
        
        while now :
            if now.val == val :
                prev.next = now.next
            else :
                prev = now
            now = now.next
        
        return prev_head.next
