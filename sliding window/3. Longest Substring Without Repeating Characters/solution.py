class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0

        maxLen = 0
        for char in s:
            while char in s[l:r]:
                l+=1
            r+=1
            maxLen = max(r-l,maxLen)
        
        return maxLen
        