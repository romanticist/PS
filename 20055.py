N, K = map(int, input().split())
A = list(map(int, input().split()))
up, stage, k_cnt, Robots = 0, 0, A.count(0), [0 for _ in range(2*N)]

while k_cnt < K:
    stage += 1
    up = (up-1+(2*N))%(2*N)
    down = (up+N-1)%(2*N)
    Robots[down] = 0

    for i in range(N-1):
        now = (down-1-i+(2*N))%(2*N)
        nex = (now+1)%(2*N)

        if [Robots[now], Robots[nex]] == [1, 0] and A[nex] > 0:
            A[nex] -= 1
            Robots[nex], Robots[now] = 1, 0
            if A[nex] == 0:
                k_cnt += 1
            if nex == down:
                Robots[nex] = 0

    if Robots[up] == 0 and A[up] > 0:
        Robots[up] = 1
        A[up] -= 1
        if A[up] == 0:
            k_cnt += 1

print(stage)


