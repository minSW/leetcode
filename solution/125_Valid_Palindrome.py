class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_s = [x for x in s.lower() if x.isalnum()]
        test_s = "".join(test_s)
        return test_s == test_s[::-1]

