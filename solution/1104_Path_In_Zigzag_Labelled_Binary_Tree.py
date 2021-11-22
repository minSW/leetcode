class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        level = len(str(bin(label))) - 3
        index = label - (1 << level) if level % 2 == 0 else (1 << (level+1)) - label - 1
        
        for i in range(level-1, -1, -1) :
            index = index >> 1
            if i % 2 == 0 :
                res.append((1 << i) + index)
            else :
                res.append((1 << (i + 1)) - index - 1)
        
        return res[::-1]
