import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A,B,C = map(int,input().split())
N = int(input())
array = [0] * 20
chk, ans = True, 0

def sol(a,b,c,x):
    global array, chk, ans
    if x == -1:
        if a*b*c > 0:
            chk = False
        return    

    f = 2**x
    if array[x] == 0 or a < f or b < f or c < f:
        sol(a,b,c,x-1)
        return
    array[x] -= 1
    ans += 1
    sol(a-f,b,c,x)
    sol(f,f,c-f,x)
    sol(f,b-f,c,x)

for _ in range(N):
    a,b = map(int,input().split())
    array[a] += b
sol(A,B,C,N-1)
if chk:
    print(ans)
else:
    print(-1)