class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        xor = [arr[0]]
        
        for x in arr[1:] :
            xor.append(xor[-1] ^ x)
        
        for i in range(n-1) :
            for k in range(i+1, n) :
                xor[k] ^= xor[i]
                if arr[i] == xor[k] :
                    res += k - i
        
        return res
