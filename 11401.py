N, K  = map(int, input().split())
tmp, ans, MOD, FERMAT = 1, 1, 1000000007, 1000000005
# k fac
for i in range(2,K+1):
    tmp *= i
    tmp %= MOD

# k!^(p-2)
while FERMAT:
    if FERMAT%2:
        ans *= tmp
        ans %= MOD
    tmp *= tmp
    tmp %= MOD
    FERMAT //= 2

# n * (n-1) * ... * (n-k+1)
for i in range(N,N-K,-1):
    ans *= i
    ans %= MOD

print(ans) 
