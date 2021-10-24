class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join([ c for c in s if not c in "aeiou"])
