N = int(input())
ans = {"AC":0,"WA":0,"TLE":0,"RE":0}
for i in range(N):
    state = input()
    ans[state] += 1
for key,val in ans.items():
    print(f"{key} x {val}")
