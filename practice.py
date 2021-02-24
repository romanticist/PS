from collections import deque

arr = deque()
for i in range(5):
    arr.append(i)

arr.popleft()
print(arr)
print("hi " + str(arr[-1]))
