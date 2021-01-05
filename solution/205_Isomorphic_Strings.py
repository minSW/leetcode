class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_t = dict()
        for i in range(0, len(s)) :
            value = t[i]
            if value in dict_t :
                dict_t[value].append(i)
            else :
                dict_t[value] = [i]
        
        checked = set()
        for index_li in dict_t.values() :
            target = s[index_li[0]]
            if target in checked :
                return False
            for i in index_li :
                if s[i] != target :
                    return False
            checked.add(target)
                
        return True
