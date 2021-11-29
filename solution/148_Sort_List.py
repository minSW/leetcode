# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        second = self.getMidNode(head)
        return self.mergeList(self.sortList(head), self.sortList(second))
    
    def getMidNode(self, head: ListNode) -> ListNode: 
        fast = head
        while True :
            fast = fast.next.next
            if not fast or not fast.next :
                break
            head = head.next
        
        head.next, res = None, head.next
        return res
    
    def mergeList(self, left: ListNode, right: ListNode) -> ListNode:
        root = node = ListNode(0)
        
        while left or right :
            if not left or not right :
                node.next = right if not left else left
                break
            elif left.val < right.val :
                node.next = left
                node, left = node.next, left.next
            else :
                node.next = right
                node, right = node.next, right.next
        
        return root.next
