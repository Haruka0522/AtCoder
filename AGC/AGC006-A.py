N = int(input())
s = input()
t = input()
flag = True
for i in range(N):
    if s[i:] == t[:(N-i)]:
        flag = False
        break
if flag:
    print(len(s + t))
elif i == 0:
    print(len(s))
else:
    print(len(s[:i]) + N)
