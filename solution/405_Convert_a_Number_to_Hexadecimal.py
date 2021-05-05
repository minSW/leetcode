class Solution:
    def toHex(self, num: int) -> str:
        hex_str = ["a", "b", "c", "d", "e", "f"]
        result = ""
        
        if num == 0 :
            result = "0"
        elif num < 0 :
            num += 2 ** 32
        
        while num > 0 :
            remain = num % 16
            result += str(remain) if remain < 10 else hex_str[remain-10]
            num = num // 16
        return result[::-1]
