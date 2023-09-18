import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #O(n) space
        #O(n) time
        
        table = collections.defaultdict(list)
        for string in strs:
            s = ''.join(sorted(string))
            table[s].append(string)
        
        res = []
        for key, val in table.items():
            res.append(val)
        
        return res

s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))