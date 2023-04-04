class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if stack and stack.pop() == char:
                    pass
                else:
                    return False
                
        return False if len(stack) else True
