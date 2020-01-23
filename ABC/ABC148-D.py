"""TLE
N = int(input())
A_list = list(map(int, input().split()))
i = 0
while(True):
    try:
        if A_list[i] != i+1:
            del A_list[i]
        else:
            i += 1
    except:
        if A_list == []:
            print(-1)
        else:
            print(N-len(A_list))
        exit()
"""

N = int(input())
A_list = list(map(int, input().split()))
iirenga = 1
kudaita = 0
for i in range(N):
    if A_list[i] == iirenga:
        iirenga += 1
    else:
        kudaita += 1
if kudaita == N:
    print(-1)
    exit()
print(kudaita)
