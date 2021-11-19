# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head :
            return None
        elif not head.next :
            return TreeNode(head.val)
        
        prev = slow = fast = head
        while fast and fast.next :
            prev, slow, fast = slow, slow.next, fast.next.next
        
        prev.next = None
        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))        
        
