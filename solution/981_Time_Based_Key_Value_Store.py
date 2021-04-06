class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map :
            self.map[key] = [(timestamp, value)]
        else :
            self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # binary search
        def binary_search(li: list) -> int:
            l, r = 0, len(values)
            while l < r :
                mid = (l + r) // 2
                if values[mid][0] <= timestamp :
                    l = mid + 1
                else :
                    r = mid
            return r
            
        if key in self.map :
            values = self.map[key]
            i = binary_search(values)
            
            if i > 0 :
                return values[i-1][1] 
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
