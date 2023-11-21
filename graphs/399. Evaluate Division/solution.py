class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        graph = defaultdict(dict)

        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)
        # dfs
        
        res = []

        def dfs(x,y,visit):
            if x not in graph or y not in graph:
                return -1.0
            
            if y in graph[x]:
                return graph[x][y]
            
            for child in graph[x]:
                if child in visit:
                    continue
                
                visit.add(child)
                temp = dfs(child,y,visit)
                if temp != -1:
                    return graph[x][child] * temp

            return -1
        for query in queries:
            res.append(dfs(query[0],query[1],set()))
        return res