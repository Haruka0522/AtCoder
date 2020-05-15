X = input()
S = list(input())
ans = []
for i in S:
    if i != X:
        ans.append(i)
print("".join(ans))
