class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one, two = 0, len(numbers) - 1
        while one < two :
            if numbers[one] + numbers[two] == target :
                return [one + 1, two + 1]
            elif numbers[one] + numbers[two] > target :
                two -= 1
            else :
                one += 1
        
