class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # O(n logn) time
        # O(n) space
        
        if len(hand) % groupSize != 0:
            return False
        cnt = {}
        for i in hand:
            cnt[i] = cnt.get(i,0) + 1
    
        hand.sort()

        for n in hand:
            if cnt[n] == 0:
                continue
            
            for j in range(groupSize):
                curr = n + j
                if cnt.get(curr,0) == 0:
                    return False
                cnt[curr] -= 1
        return True