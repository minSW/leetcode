class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        indices = [ x for x in s if x.isalpha() ]
        return "".join([ x if not x.isalpha() else indices.pop() for x in s ])
