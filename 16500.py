S = input()
N = int(input())
A = list()
D = [0]*130
D[0] = 1
for _ in range(N):
    A.append(input())
for i in range(len(S)):
    if D[i] == 1:
        for j in range(len(A)):
            if len(S) < i + len(A[j]):
                continue
            elif S[i:i+len(A[j])] == A[j]:
                D[i+len(A[j])] = 1
print(D[len(S)])
