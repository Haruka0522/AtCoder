N = int(input())
bag = []
for i in range(N):
    a = list(input().split())
    a[0] = int(a[0])
    if a[1] == "R":
        a[1] = "B"
    else:
        a[1] = "R"
    a[1],a[0] = a[0],a[1]
    bag.append(a)
bag.sort()
for i in bag:
    print(i[1])

