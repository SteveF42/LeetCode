class Solution:
    def topKFrequent(self, nums: list[int], k:int) ->list[int]:
        #bucket sort type solution
        #size complexity O(n)
        #space complexity O(n + n)
        
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     history = {}

    #     for i in nums:
    #         if i in history:
    #             history[i] += 1
    #         else:
    #             history[i] = 1

    #     values = history.items()
    #     s = sorted(values,key=lambda x: x[1]) O(nlogn)

    #     res = []
    #     for i in range(1,k+1):
    #         res.append(s[-i][0])

    #     return res