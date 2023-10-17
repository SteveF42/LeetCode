class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # O(n * k^9) n being the size of the array sum, digits 1-9 are used so 9 possiblities
        # O(k) space excluding result array
        res = []
        def dfs(i,arr):
            if len(arr) == k and sum(arr) == n:
                res.append(arr[::])
            if sum(arr) > n or len(arr) > k:
                return
            
            for j in range(i,10):
                arr.append(j)
                dfs(j+1,arr)
                arr.pop()
        
        dfs(1,[])
        return res