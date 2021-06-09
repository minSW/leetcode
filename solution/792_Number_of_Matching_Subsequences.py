class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_dict = { c : [] for c in set(s) }
        for w in words :
            if w[0] in char_dict :
                char_dict[w[0]].append(w)
        
        count = 0
        for c in s :
            candi_words = char_dict[c]
            char_dict[c] = []
            for word in candi_words :
                if len(word) == 1 : 
                    count += 1
                elif word[1] in char_dict  :
                    char_dict[word[1]].append(word[1:])
            
        return count
    
    # Time Limited Solution
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         char_dict = dict()
#         for i, c in enumerate(s) :
#             if c in char_dict :
#                 char_dict[c].append(i)
#             else :
#                 char_dict[c] = [i]
        
#         count = 0
#         for w in words :
#             index = -1
#             res = True
#             for c in w :
#                 if not c in char_dict :
#                     res = False
#                     break
#                 can = [ i for i in char_dict[c] if i  > index ]
#                 if not can :
#                     res = False
#                     break
#                 index = min(can)
             
#             if res :
#                 count += 1
#         return count
