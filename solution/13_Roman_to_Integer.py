class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sub_instances = {"CM" : 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        
        i = 0
        result = 0
        while i < len(s):
            if i != len(s) - 1 and s[i:i+2] in sub_instances:
                result += sub_instances[s[i:i+2]]
                i += 2
            else :
                result += symbols[s[i]]
                i += 1
        return result
