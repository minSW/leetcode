class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        rank, rank_dict, result  = 0, dict(), list()
        
        for i in arr2 :
            if not i in rank_dict :
                rank += 1
            rank_dict[i] = rank
        
        for i in arr :
            result.append(rank_dict[i])
        
        return result
