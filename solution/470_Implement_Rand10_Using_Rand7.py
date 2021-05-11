# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        res = 40
        while res >= 40 :
            res = (rand7() - 1) * 7 + rand7() - 1
        
        # 0 ~ 39 (40)
        return res % 10 + 1
    
    # Wrong Solution
    # def rand10(self):
    #     result = [ (i * 7 + rand7() - 1) // 5 + 1 for i in range(7) ]
    #     return result[rand7()-1]
