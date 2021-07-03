class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    
class MyHashMap:
    
    M = 10 ** 3

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None] * MyHashMap.M

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % MyHashMap.M   # getHashKey()
        
        if not self.nodes[k] :
            self.nodes[k] = Node(key, value)
            return
        
        node = self.nodes[k]
        while node :
            if node.key == key :
                node.value = value
                break
            elif not node.next :
                node.next = Node(key, value)
                break
            node = node.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % MyHashMap.M
        
        if not self.nodes[k] :
            return -1
        
        node = self.nodes[k]
        while node :
            if node.key == key :
                return node.value
            elif not node.next :
                break
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = key % MyHashMap.M
        
        if not self.nodes[k] :
            return
        elif self.nodes[k].key == key :
            self.nodes[k] = self.nodes[k].next
            return
        
        prev = node = self.nodes[k]
        while node :
            if node.key == key :
                prev.next = node.next
                return
            elif not node.next :
                return
            prev, node = node, node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
