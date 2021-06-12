class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x: int, y: int):
            a, b = max(x, y), min(x, y)
            while b != 0 :
                a, b = b, a % b
            return a

        counter, k = Counter(deck), 0
        for c in counter :
            if counter[c] == 1 :
                return False
            elif k == 0 :
                k = counter[c]
            else :
                min_k = gcd(counter[c], k)
                if min_k > 1 :
                    k = min_k
                else :
                    return False
        return True
