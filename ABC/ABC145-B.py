N = int(input())
S = list(input())
if S[:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")
