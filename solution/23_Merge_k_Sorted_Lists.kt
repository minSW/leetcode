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
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.isEmpty() || lists.all { it == null }) {
            return null
        }

        var result : ListNode? = null
        var now : ListNode? = null
        val minMap = HashMap<Int, Int>() // index : minimum

        for ((index, value) in lists.withIndex()) {
            value?.let {
                minMap[index] = it.`val`
            }
        }

        while (true) {
            var min : Int? = null
            var minIndices = mutableListOf<Int>()

            for ((key, value) in minMap) {
                if (min == null || min > value) {
                    min = value
                    minIndices = mutableListOf(key)
                } else if (min == value) {
                    minIndices.add(key)
                }
            }

            if (minIndices.isEmpty())
                break

            minIndices.map {
                var next = ListNode(lists[it]!!.`val`)
                if (result == null) {
                    result = next
                    now = result
                } else {
                    now!!.next = next
                    now = now!!.next
                }

                if (lists[it]!!.next != null) {
                    lists[it] = lists[it]!!.next
                    minMap[it] = lists[it]!!.`val`
                } else {
                    lists[it] = null
                    minMap.remove(it)
                }
            }
        }

        return result
    }
}
