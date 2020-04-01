N = int(input())
name = []
num = []
for i in range(N):
    S,P = input().split()
    name.append(S)
    num.append(P)
num = [int(i) for i in num]
if max(num) > sum(num)/2:
    print(name[num.index(max(num))])
else:
    print("atcoder")
