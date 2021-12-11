class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        islower = [ w.islower() for w in word ]
        if islower[0] :
            return all(islower)
        else :
            return len(set(islower[1:])) <= 1
