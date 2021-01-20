/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun getIntersectionNode(headA:ListNode?, headB:ListNode?):ListNode? {
        var result : ListNode? = null
        
        var a = headA
        while (a != null) {
            var b = headB
            while (b != null) {
                if (a == b) {
                    result = a
                    break
                }
                b = b.next
            }
            if (result != null) break
            a = a.next
        }
        
        return result

    }
}
