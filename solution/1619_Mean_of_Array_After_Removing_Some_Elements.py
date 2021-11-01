class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        remove = int(n * 0.05)
        return sum(arr[remove:n-remove]) / (n - 2 * remove)
