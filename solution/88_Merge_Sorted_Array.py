class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        last_index = m
        while True:
            if j == n or i == last_index :
                nums1[last_index:] = nums2[j:]
                break
            elif nums1[i] <= nums2[j]:
                i += 1
            else :
                nums1.pop()
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                last_index += 1
                
