# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        now, length = head, 0
        while now != None :
            length += 1
            now = now.next
        
        reverse, now = None, head
        for i in range(0, length // 2) :
            reverse, reverse.next, now = now, reverse, now.next

        if length % 2 != 0 :
            now = now.next
        
        while now and reverse :
            if now.val != reverse.val :
                return False
            now, reverse = now.next, reverse.next
        
        return True
