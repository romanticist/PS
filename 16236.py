from collections import deque

N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
dx, dy = (-1,0,1,0), (0,1,0,-1)

sharksize, gauge, position, totalans = 2, 0, [-1,-1], 0

for i in range(N):
    for j in range(N):
        if M[i][j] is 9:
            position = [i,j]

def solve():
    global M, sharksize, gauge, position, totalans
    q, v, c, chk = deque(), [[0 for _ in range(N)] for _ in range(N)], [], 0
    q.append([position[0],position[1]])
    v[position[0]][position[1]] = 1
    while q:
        x, y = q[0][0], q.popleft()[1]
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if v[nx][ny] == 0 and M[nx][ny] <= sharksize:
                v[nx][ny] = v[x][y] + 1
                q.append([nx,ny])
                if 0 < M[nx][ny] < sharksize:
                    c.append([v[nx][ny]-1,nx,ny])
    if not c:
        print(totalans)
        return False

    target = sorted(c)[0]
    M[position[0]][position[1]] = 0
    position = [target[1],target[2]]
    gauge+=1
    if gauge == sharksize:
        gauge = 0
        sharksize+=1

    totalans+=target[0]
    M[position[0]][position[1]] = 9
    return True

while solve():
    pass