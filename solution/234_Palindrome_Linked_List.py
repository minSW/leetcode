# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        now = head
        length = 0
        while now != None :
            length += 1
            now = now.next
        
        stack = list()
        now = head
        for i in range(0, length // 2) :
            stack.append(now.val)
            now = now.next
        
        if length % 2 != 0 :
            now = now.next
        
        while now != None :
            if now.val != stack[-1] :
                return False
            stack.pop()
            now = now.next
        
        return True
