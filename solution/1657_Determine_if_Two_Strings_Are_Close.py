class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) :
            return False
        
        char_dict, w1_list, w2_list = dict(), list(), list()
        
        for w in word1 :
            if not w in char_dict :
                char_dict[w] = [1, 0]
            else :
                char_dict[w][0] += 1
        
        for w in word2 :
            if not w in char_dict :
                return False
            else:
                char_dict[w][1] += 1
        
        for ele in char_dict.values() :
            if ele[1] == 0 :
                return False
            w1_list.append(ele[0])
            w2_list.append(ele[1])
        
        return sorted(w1_list) == sorted(w2_list)
