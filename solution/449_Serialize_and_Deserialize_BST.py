# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root :
            return ""
        return " ".join([str(root.val), self.serialize(root.left), self.serialize(root.right)]) if root.left or root.right else str(root.val)
    

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split(' ')
        if not data or data[0] == "" : 
            return None
        
        node = TreeNode(int(data.pop(0)))
        
        if data :
            i = 0
            while i < len(data) :
                if data[i] != "" and int(data[i]) > node.val :
                    break
                i += 1
            node.left = self.deserialize(' '.join(data[:i]))
            node.right = self.deserialize(' '.join(data[i:]))
        
        return node

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
