class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        
        while i < length and n > 0 :
            if flowerbed[i] == 1 :
                i += 2
            elif i == length - 1 or (i < length - 2 and flowerbed[i+1] != 1) :
                i += 2
                n -= 1
            else :
                i += 1
        
        return n == 0
