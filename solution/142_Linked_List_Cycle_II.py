# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    # Floyd's Cycle Detection Algorithm
    - x (head ~ pos), y (pos ~ meeting point), z (meeting point ~ pos)
    - y + z = cycle
    ...
    => x = c * (y+z) + z
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True :
            if not slow or not fast or not fast.next :
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                break   # (meeting point)
        
        while slow != head :
            head = head.next
            slow = slow.next
        
        return slow
        
    # simple solution - set(), O(n) memory
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     now, history = head, set()
    #     while now :
    #         if not now in history :
    #             history.add(now)
    #         else :
    #             return now
    #         now = now.next
    #     return None
