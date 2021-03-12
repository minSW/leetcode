class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = list()
        for sub in words:
            for target in words:
                if sub != target and target.find(sub) != -1 :
                    result.append(sub)
                    break
        return result
