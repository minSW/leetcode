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
    fun binaryTreePaths(root: TreeNode?): List<String> {
        val path = mutableListOf<String>()
        if (root?.`val` == null)
            return path

        root.left?.let { 
            binaryTreePaths(it).forEach{ e -> path.add("${root.`val`}->$e") }
        }
        root.right?.let {
            binaryTreePaths(it).forEach{ e -> path.add("${root.`val`}->$e") }
        }
        
        if (path.isEmpty())
            path.add("${root.`val`}")
        return path
    }
}
