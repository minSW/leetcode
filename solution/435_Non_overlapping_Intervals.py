class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res, active_end = 0, float('-inf')
        intervals.sort(key=lambda x: x[1])
        
        for start, end in intervals :
            if start < active_end :
                res += 1
            else :
                active_end = end
        
        return res
    
#     # Time Limit Exceeded Solution
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         checked = collections.defaultdict(list)
#         for i, interval in enumerate(intervals) :
#             for x in range(interval[0], interval[1]) :
#                 checked[x].append(i)
        
#         overlapped = [ indices for indices in checked.values() if len(indices) > 1 ]
        
#         def bfs(path: Set[int], index: int) -> int :
#             if index == len(overlapped) :
#                 return len(path)
            
#             res = [ bfs(set(list(path) + overlapped[index][:i] + overlapped[index][i+1:]), index+1) for i, x in enumerate(overlapped[index]) if not x in path ]
            
#             return min(res) if res else bfs(path, index+1)
        
#         return bfs([], 0)
