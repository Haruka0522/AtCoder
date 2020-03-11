N,L = map(int,input().split())
strs = [input() for i in range(N)]
strs.sort()
print("".join(strs))
