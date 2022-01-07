# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next :
            second, next_pair = head.next, self.swapPairs(head.next.next)
            head.next, second.next = next_pair, head
            return second
        return head
