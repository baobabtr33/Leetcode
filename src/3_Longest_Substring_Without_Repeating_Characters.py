class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        # 본 문제의 특이점: 
        #   counter을 통해, dict에 새로운 key를 쉽게 넣을 수 있음
        #   sliding window는 right가 늘어나면서 expand하기도 하지만,
        #       그만큼 left가 늘어나면서 shrink 되는 부분도 생각해야 됨
        #       shrink를 할때, dict를 어떻게 바꿀 것인지에 대한 생각. 
        
        # sliding window가 lagging 하면서
        
        left, right = 0, 0
        chars = collections.Counter()
        ret = 0
        
        while right < len(s):
            chars[s[right]] += 1
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1
            
            right += 1
            ret = max(ret, right-left)

        return ret
