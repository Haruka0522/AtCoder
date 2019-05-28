'''WA code
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
'''

'''WA code
#N == 100のときの処理がない
D,N = map(int,input().split())
if D==0:
    print(N)
elif D==1:
    print(N*100)
else:
    print(N*10000)
