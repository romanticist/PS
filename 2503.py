N , F , C, res = int(input()), [], [False for i in range(10)], 0
for i in range(N):
    F.append(list(map(int,input().split())))
for i in range(123,1000):
    I, chk = [i//100, (i//10)%10, i%10], True
    if I[0] == I[1] or I[1] == I[2] or I[0] == I[2] or I[0] == 0 or I[1] == 0 or I[2] == 0: 
        continue
    for j in range(N):
        strike , ball = 0, 0
        for k in range(3):
            if I[k] == int(str(F[j][0])[k]):
                strike += 1
            elif I[k] == int(str(F[j][0])[(k+1)%3]) or I[k] == int(str(F[j][0])[(k+2)%3]):
                ball += 1
        if strike != F[j][1] or ball != F[j][2]:
            chk = False
            break
    if chk:
        res += 1
print(res)