import bisect
N = int(input())
A_list = sorted(list(map(int,input().split())))
B_list = sorted(list(map(int,input().split())))
C_list = sorted(list(map(int,input().split())))
ans = 0
for B in B_list:
    a_cnt = bisect.bisect_left(A_list,B)
    c_cnt = len(C_list) - bisect.bisect_right(C_list,B)
    ans += a_cnt * c_cnt
print(ans)
