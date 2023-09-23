class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n) time
        # O(n) space ??? 
        
        numStack = []

        res = 0
        for i in tokens:
            if i == '+':
               num1 = numStack.pop() 
               num2 = numStack.pop()
               res = num2 + num1
               numStack.append(res) 
            elif i == '-':
                num1 = numStack.pop() 
                num2 = numStack.pop()
                res = num2 - num1
                numStack.append(res)
            elif i == '*':
                num1 = numStack.pop() 
                num2 = numStack.pop()
                res = num2 * num1
                numStack.append(res)
            elif i == '/':
                num1 = numStack.pop() 
                num2 = numStack.pop()
                res = num2 / num1
                numStack.append(int(res))
            else:
                numStack.append(int(i))
        return numStack[0]
