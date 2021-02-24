#틀린답
import sys
from collections import deque
import heapq

dx, dy = (-1,1,0,0),(0,0,-1,1)
R, C = map(int, input().split())
lake = [list(str(sys.stdin.readline().strip())) for _ in range(R)]
ans = 0

#data setting
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

#preprocessing
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

#priority-BFS

pq, V = [], [[0 for _ in range(C)] for _ in range(R)]
sx,sy = swan.pop()
heapq.heappush(pq, (0,sx,sy))
V[sx][sy] = 1
while pq:
    t,x,y = heapq.heappop(pq)
    ans = max(t,ans)
    if (x,y) == swan[0]:
        break
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0<=nx<R and 0<=ny<C and V[nx][ny] == 0:
            heapq.heappush(pq,(lake[nx][ny],nx,ny))
            V[nx][ny] = 1

print(ans)