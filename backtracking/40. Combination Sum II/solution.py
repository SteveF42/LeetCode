class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^n) every decision in the tree has 2 possible choices
        # O(????????) I'm not sure if I'm counting the result array as extra memory
        res = []
        candidates.sort()

        def dfs(pos,arr):
            if sum(arr) == target:
                res.append(arr[::])
                return
            if sum(arr) > target:
                return
            
            prev = -1
            for i in range(pos,len(candidates)):
                if prev == candidates[i]:
                    continue
                arr.append(candidates[i])
                dfs(i+1,arr)
                arr.pop()
                prev = candidates[i]        
        dfs(0,[])
        return res