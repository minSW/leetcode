class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0 :
            return False
        
        counter = dict()
        for i in nums :
            if i in counter :
                counter[i] += 1
            else :
                counter[i] = 1
        
        for n in sorted(counter.keys()) :
            if counter[n] != 0 :
                for i in range(n+1, n+k) :
                    if i in counter and counter[i] >= counter[n]:
                        counter[i] -= counter[n]
                    else :
                        return False
        
        return True
