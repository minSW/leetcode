import collections

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda a: (bin(a).count("1"), a))
    
    # def sortByBits(self, arr: List[int]) -> List[int]:
    #     res, count = list(), collections.defaultdict(list)
    #     for a in arr :
    #         count[bin(a).count("1")].append(a)
    #     for k in sorted(count.keys()) :
    #         res.extend(sorted(count[k]))
    #     return res
