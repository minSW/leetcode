class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0 : return True
        
        distance = None
        for n in nums :
            if n :
                if distance != None and distance < k : return False
                distance = 0
            elif distance != None :
                distance += 1
        
        return True

#         if k == 0 : return True
#
#         last_index, min_distance = None, None        
#         for i in range(0, len(nums)) :
#             if nums[i] :
#                 if last_index != None and (min_distance == None or i - last_index - 1 < min_distance) :
#                     min_distance = i - last_index - 1
#                 last_index = i
        
#         return min_distance == None or min_distance >= k
