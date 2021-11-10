class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        section = [[0]]
        
        for i in range(n) :
            if nums[i] == 0 :
                if section[-1][0] != i :
                    section[-1].append(i)
                    section.append([i+1])
                else :
                    section[-1][0] = i+1
            elif nums[i] < 0 :
                section[-1].append(i)
        
        section[-1].append(n)
        
        for sec in section :
            if len(sec) % 2 == 0 :
                res = max(res, sec[-1] - sec[0])
            else :
                res = max(res, sec[-2] - sec[0], sec[-1] - sec[1] - 1)
        return res
        

#     def getMaxLen(self, nums: List[int]) -> int:
#         section = []
#         negative = [[]]
        
#         start, n = 0, len(nums)
#         for i in range(n) :
#             if nums[i] == 0 :
#                 if start != i :
#                     negative.append([])
#                     section.append((start, i))
#                 start = i+1
#             elif nums[i] < 0 :
#                 negative[-1].append(i)
        
#         section.append((start, n))
        
#         res = 0
        
#         for sec, neg in zip(section, negative) :
#             if len(neg) % 2 == 0 :
#                 res = max(res, sec[1] - sec[0])
#             else :
#                 res = max(res, neg[-1] - sec[0], sec[1] - neg[0] - 1)
#         return res
