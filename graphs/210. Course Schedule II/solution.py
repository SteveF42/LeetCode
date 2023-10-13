class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(n) BFS time
        # O(2n + e) BFS space 
        # O(n + e) DFS time
        # O(3n + e) DFS space
        
        prereq = {c:[] for c in range(numCourses)}
        inEdges = [0] * numCourses

        # BFS

        for crs, pre in prerequisites:
            prereq[pre].append(crs)
            inEdges[crs] += 1
        
        q = deque()
        for pre, crs in prereq.items():
            if inEdges[pre] == 0:
                q.append(pre)
        
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)    
            for edge in prereq[curr]:
                inEdges[edge] -= 1
                if inEdges[edge] == 0:
                    q.append(edge)
        
        for deg in inEdges:
            if deg > 0:
                return[]
        return res

        # DFS
        prereq = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        

        cycle,visit = set(),set()
        res = []
        def dfs(crs):  
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for c in prereq[crs]:
                if dfs(c) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res