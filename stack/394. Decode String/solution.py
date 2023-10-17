class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ""
        stack = []
        k = 0

        for char in s:
            if char == '[':
                stack.append((current_string,k))
                current_string = ""
                k = 0
            elif char == ']':
                prev_str,prev_k = stack.pop()
                current_string = prev_str + current_string * prev_k
            elif char.isdigit():
                k = k*10 + int(char)
            else:
                current_string += char
        
        return current_string