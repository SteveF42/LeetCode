class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(nlogn + mlogn)
        # O(1) extra space excluding the pairs array
        
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            spell = spells[i]
            l = 0
            r = m - 1
            while l <= r:
                mid = (l+r) // 2
                prod = spell * potions[mid]
                if prod >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            
            pairs[i] = m - l
        return pairs