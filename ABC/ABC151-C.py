N,M = map(int,input().split())
AC_list = [0]*N
Pena_list = [0]*N
for i in range(M):
    p,s = input().split()
    p = int(p)
    if s == "WA":
        if AC_list[p-1] == 1:
            continue
        else:
            Pena_list[p-1] += 1
    else:
        AC_list[p-1] = 1
for i in range(N):
    if AC_list[i] == 0:
        Pena_list[i] = 0
print(AC_list.count(1),end=" ")
print(sum(Pena_list))
