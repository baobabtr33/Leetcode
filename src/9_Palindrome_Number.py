class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) > 8:
            return True
        return x == x[::-1]
