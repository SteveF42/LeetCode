# O(n + m) time complexity
# O(n) space complexity

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = set()
        for word in words:
            s = ''
            for c in word:
                i = ord(c) - ord('a')
                s += table[i]
            res.add(s)
        return len(res)