class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        
        shortest = min(strs, key = len)
        strs.remove(shortest)
        ret = ""

        right = 1
        while right <= len(shortest):
            flag = True
            for _str in strs:
                if shortest[:right] != _str[:right]:
                    flag = False
            if flag:
                ret = shortest[:right]
                right += 1
            else:
                break
        
        return ret
