class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_dict = dict()
        for i, s in enumerate(source) :
            if not s in s_dict : s_dict[s] = [i]
            else : s_dict[s].append(i)
        
        now_index, count = -1, 1
        for t in target:
            if not t in s_dict : 
                return -1
            
            indices = [ i for i in s_dict[t] if i > now_index ]
            if indices :
                now_index = indices[0]
            else :
                count += 1
                now_index = s_dict[t][0]
        return count
