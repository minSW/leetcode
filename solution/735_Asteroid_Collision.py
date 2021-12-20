class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ahead = []
        for i, x in enumerate(asteroids) :
            if x > 0 : 
                ahead.append(x)
                continue
            
            while ahead and 0 < ahead[-1] < abs(x) :
                ahead.pop()
            
            if not ahead or ahead[-1] < 0 :
                ahead.append(x)
            elif ahead[-1] == abs(x) :
                ahead.pop()
        
        return ahead
