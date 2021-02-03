import copy

dx, dy = (-1,-1,0,1,1,1,0,-1), (0,1,1,1,0,-1,-1,-1)
N, M, K = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(M)]
for i in range(M): F[i][0],F[i][1] = F[i][0]-1,F[i][1]-1
for _ in range(K):
    P, newF = [[[] for _ in range(N)] for _ in range(N)], []    
    for i in range(len(F)):
        x,y = (F[i][0]+F[i][3]*dx[F[i][4]])%N,(F[i][1]+F[i][3]*dy[F[i][4]])%N
        F[i][0],F[i][1] = x,y

        P[x][y].append(i)
    for i in range(N):
        for j in range(N):
            if not P[i][j]: continue
            elif len(P[i][j]) == 1: newF.append(F[P[i][j][0]])
            else:
                m,s,f,chk,l = 0,0,F[P[i][j][0]][4],True,len(P[i][j])
                for k in range(l):
                    m += F[P[i][j][k]][2]
                    s += F[P[i][j][k]][3]
                    chk *= (f%2==F[P[i][j][k]][4]%2)
                    f = F[P[i][j][k]][4]
                if not m//5: continue
                for k in range(4):
                    newF.append([i,j,m//5,s//l,(2*k)+(chk^1)])
    F = copy.deepcopy(newF)


ans = 0
for i in F: ans += i[2]
print(ans)

