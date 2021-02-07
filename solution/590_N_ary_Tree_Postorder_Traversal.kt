/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var children: List<Node?> = listOf()
 * }
 */

class Solution {
    fun postorder(root: Node?): List<Int> {
        val stack = mutableListOf<Node?>()
        val result = mutableListOf<Int>()

        if (root == null) {
            return listOf()
        }
        
        stack.add(root)

        while (stack.isNotEmpty()) {
            val now = stack[0]
            if (now?.`val` == null) {
                stack.removeAt(0)
            } else if (now?.children.isEmpty()) {
                result.add(now.`val`)
                stack.removeAt(0)
            } else {
                stack.addAll(0, now.children)
                now.children = listOf()
            }
        }
        return result
    }
}
