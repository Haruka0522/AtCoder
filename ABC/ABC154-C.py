N = int(input())
A = list(map(int,input().split()))
A_set = set(A)
if sorted(list(A_set)) == sorted(A):
    print("YES")
else:
    print("NO")
