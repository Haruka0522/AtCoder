N,M,X = map(int,input().split())
list_a = list(map(int,input().split()))
goal_0 = 0
goal_N = 0
for i in list_a:
    if i > X:
        break
    goal_0 += 1
for i in list_a[::-1]:
    if i < X:
        break
    goal_N += 1
print(min(goal_0,goal_N))
