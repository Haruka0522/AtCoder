import collections
N = int(input())
S_list = [input() for i in range(N)]
C = collections.Counter(S_list)
L = C.most_common()
max_ = L[0][1]
ans = []
#print("========")
for i in L:
    if i[1] == max_:
        ans.append(i[0])
    else:
        break
ans.sort()
for i in ans:
    print(i)
