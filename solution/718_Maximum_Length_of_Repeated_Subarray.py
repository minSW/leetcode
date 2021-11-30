class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res, n, m = 0, len(nums1), len(nums2)
        mem = [[ 0 for _ in range(m+1)] for _ in range(n+1) ]
        
        for i in range(n-1, -1, -1) :
            for j in range(m-1, -1, -1) :
                mem[i][j] = mem[i+1][j+1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res, mem[i][j])
        
        return res

    # Time Limit Exceeded Solution
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         res = 0
#         n2 = collections.defaultdict(list)
#         for i, x in enumerate(nums2) :
#             n2[x].append(i)
#         for i, x in enumerate(nums1) :
#             for j in n2[x] :
#                 cnt = 0
#                 for t in range(len(nums1)-i) :
#                     if j+t < len(nums2) and nums1[i+t] == nums2[j+t] :
#                         cnt += 1
#                     else :
#                         break
#                 res = max(res, cnt)
#         return res
