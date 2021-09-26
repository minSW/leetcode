class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(path: str, stack_cnt: int, k: int) :
            if not k and not stack_cnt :
                res.append(path)
                return
            if stack_cnt :
                dfs(path + ")", stack_cnt - 1, k)
            if k :
                dfs(path + "(", stack_cnt + 1, k - 1)
        
        dfs("", 0, n)
        return res
