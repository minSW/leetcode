class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for l in logs :
            if l == "../" and depth > 0 :
                depth -= 1
            elif l != "./" and l[0] != "." and l[-1] == "/" :
                depth += 1
        return depth
