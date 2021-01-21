# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # recursively
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
    
    # iteratively
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        now = head
        
        while now != None :
            tmp = now.next
            now.next = prev
            prev = now
            now = tmp
        
        return prev
