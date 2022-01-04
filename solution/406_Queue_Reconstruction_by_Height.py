import collections

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people :
            res.insert(p[1], p)
        return res
    
    # slow and more memory usage solution
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         heights = collections.defaultdict(list)
#         indices = [ i for i in range(len(people)) ]
        
#         for h, k in people :
#             heights[h].append(k)
        
#         for h, values in sorted(heights.items()) :
#             for i, k in enumerate(sorted(values)) :
#                 people[indices.pop(k-i)] = [h, k]
        
#         return people
