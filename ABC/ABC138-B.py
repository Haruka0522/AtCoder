N = int(input())
A_list = list(map(int,input().split()))
A_gyakusu = [1/i for i in A_list]
A_gyakusu_souwa = sum(A_gyakusu)
print(1/A_gyakusu_souwa)
