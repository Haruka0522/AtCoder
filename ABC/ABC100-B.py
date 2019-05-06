D, N = map(int, input().split())
ans = []
count = 0
while (True):
    try:
        print(ans[N])
        break
    except:
        ans.append((100 ** D) * count)
    count += 1
