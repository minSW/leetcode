class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))

#     def frequencySort(self, nums: List[int]) -> List[int]:
#         count, result = Counter(nums), list()
#         new_dict = dict()
#         for x in count.most_common() :
#             if x[1] in new_dict :
#                 new_dict[x[1]].append(x[0])
#             else :
#                 new_dict[x[1]] = [x[0]]
        
#         for k in sorted(new_dict.keys()) :
#             for i in sorted(new_dict[k], reverse=True) :
#                 result.extend([i] * k)
#         return result
