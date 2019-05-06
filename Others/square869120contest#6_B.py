# WA０点回答
N = int(input())
A_list = []
B_list = []
iriguchi_list = []
deguchi_list = []
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    A_list.append(a)
    B_list.append(b)
A_list_ave = sum(A_list) / N
B_list_ave = sum(B_list) / N
for i in A_list:
    iriguchi_list.append(abs(A_list_ave - i))
iriguchi = A_list[iriguchi_list.index(min(iriguchi_list))]
for i in B_list:
    deguchi_list.append(abs(B_list_ave - i))
deguchi = B_list[deguchi_list.index(min(deguchi_list))]
for j in range(N):
    ans += abs(A_list[j] - iriguchi) + abs(B_list[j] -
                                           A_list[j] + abs(deguchi - B_list[j]))
print(ans)
