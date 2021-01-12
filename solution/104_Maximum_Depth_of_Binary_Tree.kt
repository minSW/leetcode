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
    fun maxDepth(root: TreeNode?): Int {
        return getDepth(root, 0)
    }

    fun getDepth(node: TreeNode?, depth: Int): Int {
        if (node == null) {
            return depth
        } else if (node.left == null && node.right == null) {
            return depth + 1
        } else {
            var left = getDepth(node.left, depth + 1)
            var right = getDepth(node.right, depth + 1)
            return if (left > right) left else right
        }
    
    }
}
