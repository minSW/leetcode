class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = 10 ** 3
        self.set_arr = [ [] for _ in range(self.hash) ]

    def add(self, key: int) -> None:
        if not self.contains(key) :
            self.set_arr[self.index(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key) :
            self.set_arr[self.index(key)].remove(key)
    
    def contains(self, key: int) -> bool:
        index = self.index(key)
        return key in self.set_arr[index]
    
    def index(self, key: int) -> int :
        return key % self.hash

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
