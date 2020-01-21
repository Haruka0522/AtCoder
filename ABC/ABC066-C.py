"""TLE
N = int(input())
sequence = list(input().split())
ans = []
for i in range(N):
    a_i = sequence[i]
    ans.append(a_i)
    ans = ans[::-1]
print(" ".join(ans))
"""

from collections import deque
n = int(input())
sequence = deque(map(int,input().split()))
ans = deque()
if n % 2 == 1:
    for i in range(n):
        if i % 2 == 0:
            ans.appendleft(sequence[0])
        else:
            ans.append(sequence[0])
        sequence.popleft()
        #print(ans)
else:
    for i in range(n):
        if i % 2 == 1:
            ans.appendleft(sequence[0])
        else:
            ans.append(sequence[0])
        sequence.popleft()
        #print(ans)
print(*ans)
