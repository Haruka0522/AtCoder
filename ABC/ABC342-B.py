n = int(input())
p_list = list(map(int, input().split()))
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    for j in range(n):
        if p_list[j] == a:
            print(a)
            break
        elif p_list[j] == b:
            print(b)
            break
