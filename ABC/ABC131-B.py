N,L = map(int,input().split())
apple = [i+L for i in range(N)]
apple_abs = [abs(i) for i in apple]
del apple[apple_abs.index(min(apple_abs))]
print(sum(apple))
