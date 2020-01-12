N = int(input())
kyoku = []
fun = []
for i in range(N):
    s,t = input().split()
    t = int(t)
    kyoku.append(s)
    fun.append(t)
X = input()
for i in kyoku:
    if i == X:
        del fun[:kyoku.index(X)+1]
if fun == []:
    print(0)
else:
    print(sum(fun))
