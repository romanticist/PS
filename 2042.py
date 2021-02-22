def getsum(tree,i):
    s = 0
    while i > 0:        
        s += tree[i]
        i -= i&(-i)
    return s

def update(tree, n, i, v):
    while i <= n:
        tree[i] += v
        i += i&(-i)

N, M, K = map(int, input().split())
arr, tree = [0]*(N+1), [0]*(N+1)

for i in range(1,N+1):
    arr[i] = int(input())
    update(tree, N, i, arr[i])

for i in range(M+K):    
    a,b,c = map(int,input().split())
    if a == 1:
        d = c-arr[b]
        arr[b] = c
        update(tree,N,b,d)
    else:
        print(getsum(tree,c)-getsum(tree,b-1))