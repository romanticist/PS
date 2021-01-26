N, M = map(int, input().split())
B, ans = [list(input()) for _ in range(N)], 1000

for i in range(N-7):
    for j in range(M-7):
        c1, c2 = 0, 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if B[k][l] == 'W':
                        c1+=1
                    else:
                        c2+=1
                else:
                    if B[k][l] == 'B':
                        c1+=1
                    else:
                        c2+=1
        ans = min(ans,c1,c2)

print(ans)