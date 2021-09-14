class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = dict()
        
        def getResult(state: str) -> bool :
            if not state in memo : 
                memo[state] = False
                for i in range(len(state)-1) :
                    if state[i:i+2] == "++" and not getResult(state[:i] + "--" + state[i+2:]) :
                        memo[state] = True
                        break
            return memo[state]
        
        return getResult(currentState)
