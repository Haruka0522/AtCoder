n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

able = set()
for A in a:
    for B in b:
        for C in c:
            able.add(A+B+C)
for X in x:
    if X in able:
        print("Yes")
    else:
        print("No")
