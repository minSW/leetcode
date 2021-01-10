/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        val left = preorder(root?.left, false)
        val right = preorder(root?.right, true)

        if (left.size != right.size) {
            return false
        }
        return left.zip(right).all{ (x, y) -> x == y }
    }

    // recursively
    fun preorder(node: TreeNode?, reverse: Boolean = false): MutableList<Int?> {
        return node?.let {
            val result = mutableListOf<Int?>(it.`val`)
            if (!reverse) {
                result += preorder(it.left, reverse) + preorder(it.right, reverse)
            } else {
                result += preorder(it.right, reverse) + preorder(it.left, reverse)
            }
            return result
        } ?: mutableListOf<Int?>(null)

    }

    // iteratively
    fun preorder(node: TreeNode?, reverse: Boolean = false): MutableList<Int?> {
        val result = mutableListOf<Int?>()
        val stack = mutableListOf<TreeNode?>()
        var now = node
        while (true) {
            if (now == null) {
                result.add(null)
                if (stack.isEmpty()) {
                    break
                }
                now = if (!reverse) stack.last()?.right else stack.last()?.left
                stack.remove(stack.last())
                continue
            }
            result.add(now.`val`)
            stack.add(now)
            now = if (!reverse) now.left else now.right
        }
        return result
    }

}

