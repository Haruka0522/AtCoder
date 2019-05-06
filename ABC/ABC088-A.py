N = int(input())
A = int(input())
hituyo_coin = N%500
if(hituyo_coin > A):
    print("No")
else:
    print("Yes")