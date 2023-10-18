class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # O(n) time
        # O(2n) space
        graph = {i : [] for i in range(len(isConnected)) }
        for i,row in enumerate(isConnected):
            for j,val in enumerate(row):
                if val == 1 and i != j:
                    graph[i].append(j)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            
            visit.add(i)
            for neighbor in graph[i]:
                dfs(neighbor)
            
            return True


        print(graph)
        res = 0
        for i, arr in graph.items():
            if dfs(i):
                res += 1
        return res