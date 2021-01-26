import heapq
from collections import deque

N, ans = int(input()), 0
A, heap = [list(map(int,input().split())) for _ in range(N)], []
A.sort()
q = deque(A)
for i in range(A[-1][0], 0, -1):
    while True:
        if len(q) != 0 and i <= q[-1][0]:
            num = q.pop()[1]
            heapq.heappush(heap, (-num, num))
        else:break
    if len(heap) != 0:
        ans += heapq.heappop(heap)[1]
print(ans)