import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = next_n = len(matrix)
        heap = list()
        
        for j in range(n):
            col_bound = next_n
            for i in range(col_bound):
                # for max heap
                now = -matrix[j][i]
                
                if len(heap) == k :
                    next_n = i + 1
                if len(heap) < k:
                    heapq.heappush(heap, now)
                elif now > heap[0]:
                    # Remove max value of heap
                    heapq.heappushpop(heap, now)
        
        # for max heap
        return -heap[0]
