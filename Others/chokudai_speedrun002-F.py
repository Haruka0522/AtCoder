set_a = set()
for i in range(int(input())):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    set_a.add((a,b))
print(len(set_a))
