class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_li = list(magazine)
        for i in ransomNote :
            if i in magazine_li :
                magazine_li.remove(i)
            else :
                return False
        return True
