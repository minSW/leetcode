class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res, not_in = [], []
        dict2 = { i : 0 for i in arr2 }
        
        for a in arr1 :
            if a in dict2 :
                dict2[a] += 1
            else :
                not_in.append(a)
        
        for a in arr2 :
            res.extend([a] * dict2[a])
        
        return res + sorted(not_in)
