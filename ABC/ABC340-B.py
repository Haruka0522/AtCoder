q = int(input())
li = []
for _ in range(q):
    kind, n = map(int, input().split())
    if kind == 1:
        li.append(n)
    elif kind == 2:
        print(li[-n])
