N = int(input())
A = list(map(int,input().split()))
D , ans = [0]*N , 0
for i in range(N):
    big = 0
    for j in range(i):
        if A[i] > A[j]:
            big = max(big, D[j])
    D[i] = A[i] + big
    ans = max(D[i],ans)
print(ans)