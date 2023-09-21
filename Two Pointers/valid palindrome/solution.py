class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        def isAlphaNum(s: str)-> bool:
            if (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or
                ord('0') <= ord(s) <= ord('9')):
                return True
            return False

        while l < r:
            while not isAlphaNum(s[l]) and l < r:
                l+=1
            while not isAlphaNum(s[r]) and l < r:
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        return True
    

s = Solution()

res = s.isPalindrome(" ")
print(res)