class Solution:
    def numberOfSteps (self, num: int) -> int:
        bin_num = bin(num)[2:]
        return bin_num.count('1') + len(bin_num) - 1
    
    # def numberOfSteps (self, num: int) -> int:
    #     count = 0
    #     while num != 0 :
    #         num = num // 2 if num % 2 == 0 else num - 1
    #         count += 1
    #     return count
