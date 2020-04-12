N = int(input())
S = list(input())
R_list = [0]*(N+1)
R_list_ = []
R_cnt = 0
G_list = [0]*(N+1)
G_list_ = []
G_cnt = 0
B_list = [0]*10000
B_list_ = []
B_cnt = 0
ans = 0
for i, j in enumerate(S):
    i += 1
    if j == "R":
        R_list[i] = 1
        R_list_.append(i)
        R_cnt += 1
    elif j == "G":
        G_list[i] = 1
        G_list_.append(i)
        G_cnt += 1
    else:
        B_list[i] = 1
        B_list_.append(i)
        B_cnt += 1
for i in R_list_:
    for j in G_list_:
        if B_list[2*j-i] != 1:
            ans += B_cnt
        else:
            ans += (B_cnt - 1)
print(ans)
