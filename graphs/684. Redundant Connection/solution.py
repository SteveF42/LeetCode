class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connected = defaultdict(list)

        def dfs(x,y,visited):
            if x == y:
                return True
            for adj in connected[x]:
                if not visited[adj]:
                    visited[adj] = True
                    if dfs(adj,y,visited):
                        return True
            return False

        for edge in edges:
            x,y = edge
            visited = defaultdict(bool)
            if dfs(x,y,visited):
                return edge
            
            connected[x].append(y)
            connected[y].append(x)
