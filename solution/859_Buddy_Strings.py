class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == 1 : 
            return False
        
        i = j = None
        result = True
        
        for x in range(0, len(A)) :
            if A[x] != B[x] :
                if i == None :
                    i = x
                elif j == None :
                    j = x
                    if A[i] != B[j] or A[j] != B[i] :
                        result = False
                        break
                else :
                    result = False
                    break
        
        if (i == None and len(set(A)) == len(A)) or (i != None and j == None) :
            result = False
        
        return result
