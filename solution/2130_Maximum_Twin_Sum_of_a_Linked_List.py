# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        slow = fast = head
        stack = []
        
        while fast :
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow and stack :
            res = max(res, slow.val + stack.pop())
            slow = slow.next
        
        return res
