class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(n^m) n being the length of digits and m being the amount of characters to iterate over (it can be 3 or 4 in this case)
        #  O(9) space for the keypad
        
        if digits == "":
            return []
        res = []
        keyPad = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }

        def dfs(i,arr):
            if i >= len(digits):
                res.append(''.join(arr))
                return
           
            for char in keyPad[int(digits[i])]:    
                arr.append(char)
                dfs(i+1,arr)
                arr.pop()
        
        dfs(0,[])
        return res