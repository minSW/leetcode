class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = dict()
        for i in arr :
            if not i in occurence :
                occurence[i] = 1
            else :
                occurence[i] += 1
        return len(set(occurence.values())) == len(occurence)
