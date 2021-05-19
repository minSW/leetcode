import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res, heap = list(), list()
        max_value, end = 0, len(nums1)
        
        for j in range(len(nums2)) :
            n = end
            for i in range(n) :
                ele = (nums1[i] + nums2[j], (i, j))
                
                if len(heap) < k :
                    heapq.heappush(heap, ele)
                    max_value = max(max_value, ele[0])
                elif ele[0] <= max_value :
                    heapq.heappush(heap, ele)
                    end = i + 1
        
        while len(res) < k and heap :
            i, j = heapq.heappop(heap)[1]
            res.append([nums1[i], nums2[j]])
            
        return res

