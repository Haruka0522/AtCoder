L = list(map(int,input().split()))
cost = 0
max_L = max(L)
L.remove(max_L)
second_L = max(L)
cost = max_L - second_L
L.remove(max(L))
cost += second_L - L[0]
print(cost)
