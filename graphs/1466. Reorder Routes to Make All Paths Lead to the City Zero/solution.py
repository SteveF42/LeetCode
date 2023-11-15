class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = {i:[] for i in range(n)}

        for s,e in connections:
            graph[s].append(e)
            graph[e].append(s)
            visited.add((s,e))
        
        def dfs(node,parent):
            ans = 0
            if (parent,node) in visited:
                ans += 1
            
            for c in graph[node]:
                if c != parent:
                    ans += dfs(c,node)
            return ans
            
        return dfs(0,-1)