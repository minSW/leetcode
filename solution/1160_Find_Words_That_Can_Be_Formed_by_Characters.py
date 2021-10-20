from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        return sum(len(word) for word in words if not Counter(word) - chars_counter)
