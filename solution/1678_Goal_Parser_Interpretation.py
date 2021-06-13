class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for c in command :
            if c == "G" : res += "G"
            elif c == "(" : res += "o"
            elif c == "a" : res = res[:-1] + "al"
        return res
