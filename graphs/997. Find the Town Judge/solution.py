class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # O(n) time
        # O(n) space
        graph = [0] * (n+1)

        for arr in trust:
            graph[arr[0]] -= 1
            graph[arr[1]] += 1
            
        
        edges = [0] * n
        for i in range(1,n+1):
            if graph[i] == n-1:
                return i
        
        return -1