a,b,c = map(int,input().split())
costs = [a+b,b+c,c+a]
print(min(costs))