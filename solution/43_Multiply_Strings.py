class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = [ int(x) for x in num1[::-1] ]
        n2 = [ int(y) for y in num2[::-1] ]
        result = [0] * (len(num1) + len(num2) + 1)
        
        for j in range(len(num2)) :
            for i in range(len(num1)) :
                result[i+j] += n1[i] * n2[j]
        
        for index, m in enumerate(result) :
            if m >= 10 :
                result[index+1] += m // 10
                result[index] = str(m % 10)
            else :
                result[index] = str(m)
        
        result = result[::-1]
        while len(result) > 1 and result[0] == "0" :
            result.pop(0)
        return "".join(result)
