import copy
import sys

sys.setrecursionlimit(10000)

R = range
N, Q = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

def solve(L):
    global N, A
    C = copy.deepcopy(A)
    for i in R(0,2**N,2**L):
        for j in R(0,2**N,2**L):
            for k in R(2**L):
                for l in R(2**L):
                    A[i+l][(j+2**L-1)-k] = C[i+k][j+l]
    C2 = copy.deepcopy(A)
    for i in R(2**N):
        for j in R(2**N):
            cnt = 0
            if C2[i][j] == 0:
                continue
            for a,b in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if 0 <= a < 2**N and 0 <= b < 2**N:
                    if C2[a][b] != 0:
                        cnt+=1
            if cnt < 3:
                A[i][j] -= 1

for i in R(Q):
    solve(L[i])

V, ans, ans2 = [[0 for _ in R(2**N)] for _ in R(2**N)], 0, 0

for sub in A: ans2 += sum(sub)
print(ans2)

def dfs(x,y):
    global A, V, N
    ans = V[x][y] = 1
    for a,b in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
        if 0 <= a < 2**N and 0 <= b < 2**N and V[a][b] == 0 and A[a][b] != 0:
            ans += dfs(a,b)
    return ans

for i in R(2**N):
    for j in R(2**N):
        if V[i][j] == 0 and A[i][j] != 0:
            ans = max(dfs(i,j),ans)
print(ans)
