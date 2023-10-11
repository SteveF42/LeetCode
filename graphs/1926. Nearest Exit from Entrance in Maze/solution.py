class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque() # [int,int,step]
        q.append([entrance[0],entrance[1],0])
        visited = set() # (int,int)

        while q:
            r,c,step = q.popleft()
            
            if r >= len(maze) or r < 0 or c >= len(maze[r]) or c < 0 or ((r,c) in visited) or maze[r][c] == '+':
                continue
            
            if (([r,c] != entrance) and 
                (r == 0 or c == 0 or r==len(maze)-1 or c==len(maze[r])-1 )):
                return step

            visited.add((r,c))
            q.append([r+1,c,step+1])
            q.append([r-1,c,step+1])
            q.append([r,c+1,step+1])
            q.append([r,c-1,step+1])

        return -1