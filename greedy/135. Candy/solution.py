class Solution:
    def candy(self, ratings: List[int]) -> int:
        # O(n logn) time
        # O(n) space
        data = [(x,i) for i,x in enumerate(ratings)]
        data.sort()
        res = [1] * len(ratings)

        for x,i in data:

            if i > 0 and ratings[i] > ratings[i-1]:
                res[i] = max(res[i],res[i-1] + 1)

            if i < len(ratings)-1 and ratings[i] > ratings[i+1]:
                res[i] = max(res[i],res[i+1]+1)
        
        return sum(res)