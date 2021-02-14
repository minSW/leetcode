class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set(arr)
        for i in arr :
            if i == 0 :
                if 0 in arr_set :
                    arr_set.remove(0)
                else :
                    return True
            if i * 2 in arr_set :
                return True
        return False
