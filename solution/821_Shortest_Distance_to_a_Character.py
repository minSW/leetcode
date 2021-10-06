class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_index = [ i for i, x in enumerate(s) if x == c ]
        res, index = [], 0
        for i in range(len(s)) :
            if not index :
                res.append(abs(c_index[index]-i))
            else :
                res.append(min(abs(i-c_index[index-1]), abs(c_index[index]-i)))
            if c_index[index] == i and index < len(c_index) - 1 :
                index += 1
        return res
