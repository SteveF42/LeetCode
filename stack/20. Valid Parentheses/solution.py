class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time
        # O(n) space
        stack = []
        if(len(s) <= 1):
            return False
        
        for br in s:
            if br == '(' or br == '{' or br == '[':
                stack.append(br)
            elif len(stack) == 0: 
                return False
            elif stack[-1] == '(' and br == ')':
                stack.pop()
            elif stack[-1] == '[' and br == ']':
                stack.pop()
            elif stack[-1] == '{' and br == '}':
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
                