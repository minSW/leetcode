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
}
