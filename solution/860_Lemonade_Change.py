class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pos = [0, 0] # 5, 10
        
        for i in bills :
            if i == 5 :
                pos[0] += 1
            elif i == 10 and pos[0] > 0 :
                pos[0] -= 1
                pos[1] += 1
            elif i == 20 and pos[1] > 0 and pos[0] > 0 :
                pos[1] -= 1
                pos[0] -= 1
            elif i == 20 and pos[0] > 3 :
                pos[0] -= 3
            else :
                return False
        
        return True
