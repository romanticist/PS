import sys
from collections import deque
import heapq

dx, dy = (-1,1,0,0),(0,0,-1,1)
R, C = map(int, input().split())
lake = [list(str(sys.stdin.readline().strip())) for _ in range(R)]
ans = 0

#data setting 1500 * 1500
swan, water = deque(), deque()
for x in range(R):
    for y in range(C):
        if lake[x][y] == 'L':
            swan.append((x,y))
            water.append((x,y))
            lake[x][y] = 0
        elif lake[x][y] == '.':
            water.append((x,y))
            lake[x][y] = 0

#preprocessing 1500*1500
time = 1
while water:
    tmp = deque()
    while water:        
        x,y = water.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<R and 0<=ny<C and lake[nx][ny] == 'X':
                lake[nx][ny] = time
                tmp.append((nx,ny))
    water = tmp
    time+=1

#print
# for x in lake:
#     for y in x:
#         print(y, end="")
#     print()

#BFS
def swan_bfs(K):
    global lake, swan    
    q, V = deque(), [[0 for _ in range(C)] for _ in range(R)]
    sx, sy = swan[1]    
    q.append((sx,sy))
    V[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if (x,y) == swan[0]:                            
            return True
        for k in range(4):
            nx, ny = x+dx[k],y+dy[k]
            if 0 <= nx < R and 0 <= ny < C and V[nx][ny] == 0 and lake[nx][ny] <= K:
                V[nx][ny] = 1
                q.append((nx,ny))
    return False

#binary search
l,r = 0, 1600
while l <= r:
    m = (l+r)//2    
    if swan_bfs(m):
        ans = m
        r = m-1        
    else:
        l = m+1

print(ans)