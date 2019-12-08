#WAコード
A,B,X = map(int,input().split())
ans = 0
for i in reversed(range(111111112)):
    if A*i + B*(len(str(i))) < X:
        ans = i
        break
print(ans)
