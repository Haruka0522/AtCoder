N = int(input())
N_li = list(str(N))
N_SUM = sum(map(int,N_li))
if(N % N_SUM == 0):
    print("Yes")
else:
    print("No")