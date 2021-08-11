class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = { x : i for i, x in enumerate(order) }
        res = [[ alien_dict[c] for c in word ] for word in words ]
        return res == sorted(res)
