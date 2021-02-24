class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result, left, right = list(), 0, len(arr)
        
        for i in range(len(arr)) :
            if x > arr[i] :
                left = i
            elif x == arr[i] :
                left, right = i, i+1
                break
            else :
                right = i
                break
        
        while k > 0 :
            if left < 0 or right == 0 :
                result.extend(arr[right:right+k])
                break
            elif right >= len(arr) :
                result.extend(arr[left-k+1:left+1])
                break
            elif x - arr[left] <= arr[right] - x :
                result.append(arr[left])
                left -= 1
            else :
                result.append(arr[right])
                right += 1
            k -= 1
        
        return sorted(result)
