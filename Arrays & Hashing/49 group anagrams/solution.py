import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #O(n) space
        #O(n * klogk) time where k is average length of string

        table = collections.defaultdict(list)
        for string in strs: #O(n)
            s = ''.join(sorted(string)) #O(klogk)
            table[s].append(string)
        
        res = []
        for key, val in table.items():
            res.append(val)
        
        return res

s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))