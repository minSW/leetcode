# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = None
        res = None
        while l1 is not None:
            if l2 is None or l1.val <= l2.val :
                if start == None:
                    start = l1
                    res = l1
                else:
                    res.next = l1
                    res = res.next
                l1 = l1.next
            else :
                if start == None:
                    start = l2
                    res = l2
                else:
                    res.next = l2
                    res = res.next
                l2 = l2.next
        if l2 is not None:
            if start == None:
                start = l2
            else:
                res.next = l2
        return start


