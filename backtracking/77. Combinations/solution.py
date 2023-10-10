class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # O(2^n) time complexity
        # O(k) where k is the temp array in the backtrack function
        res = []

        def backtrack(i,arr):
            if len(arr) == k:
                res.append(arr[::])
                return
            
            for j in range(i,n+1):
                arr.append(j)
                backtrack(j+1,arr)
                arr.pop()
        
        backtrack(1,[])
        return res