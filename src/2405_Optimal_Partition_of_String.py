class Solution:
    def partitionString(self, s: str) -> int:
        unique = set()
        cnt = 1
        for char in s:
            if char in unique:
                unique = set()
                cnt +=1 
            unique.add(char)
        return cnt
