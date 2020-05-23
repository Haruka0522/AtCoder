from math import floor
N = int(input())
mat = [set(input()) for _ in range(N)]
ans = []

if N % 2 == 1:
    for i in range(N//2):
        intersection = mat[i] & mat[-i-1]
        if intersection == set():
            print(-1)
            exit()
        ans.append(list(intersection)[0])
    print("".join(ans)+list(mat[N//2])[0]+"".join(ans[::-1]))
else:
    for i in range(N//2):
        intersection = mat[i] & mat[-i-1]
        if intersection == set():
            print(-1)
            exit()
        ans.append(list(intersection)[0])
    print("".join(ans)+"".join(ans[::-1]))

