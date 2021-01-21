# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tail = head
        while tail != None and tail.next != None :
            tail = tail.next
        
        self.reverse(head)
        return tail
        
    def reverse(self, node: ListNode) -> ListNode:
        if node == None or node.next == None :
            return node
        result = self.reverse(node.next)
        result.next = ListNode(node.val)
        return result.next
