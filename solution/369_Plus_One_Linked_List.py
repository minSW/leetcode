# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def carry(node: ListNode) -> int :
            if not node : 
                return 1
            
            node.val += carry(node.next)
            if node.val == 10 :
                node.val = 0
                return 1
            return 0
        
        return head if not carry(head) ListNode(1, head)
