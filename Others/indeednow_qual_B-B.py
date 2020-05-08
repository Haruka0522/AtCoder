from collections import deque
s = input()
t = input()
if len(s) != len(t):
    print(-1)
    exit()
s = deque(s)
t = deque(t)
for i,moji in enumerate(t):
    #print(s)
    if s == t:
        print(i)
        exit()
    s.appendleft(s[-1])
    s.pop()
