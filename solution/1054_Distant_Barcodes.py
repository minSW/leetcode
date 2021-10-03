from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        barcodes.sort(key=lambda x: (-counter[x], x))
        i, res = 0, [0] * len(barcodes)
        for x in barcodes :
            res[i] = x
            if i + 2 < len(barcodes) : i += 2
            else : i = 1
        return res


#     # Time Limit Exceeded
#     def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
#         counter = Counter(barcodes)
#         barcodes.sort(key=lambda x: -counter[x])
#         n = len(barcodes)
        
#         def canSwap(i, j) :
#             if barcodes[i] == barcodes[j] : return False
#             elif i > j :
#                 if j > 0 and barcodes[i] == barcodes[j-1] : return False
#                 if j < n - 1 and barcodes[i] == barcodes[j+1] : return False
#             return True
        
#         for i in range(1, n) :
#             if barcodes[i] == barcodes[i-1] :
#                 j = (i + 1) % n
#                 while not canSwap(i, j) :
#                     j = (j + 1) % n
#                 barcodes[i], barcodes[j] = barcodes[j], barcodes[i]
        
#         return barcodes
