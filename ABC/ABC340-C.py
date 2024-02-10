n = int(input())
ans = 0

dic = {2: 2, 1: 0}
def f(x):
    if None != dic.get(x):
        # あったら
        return dic[x]
    else:
        dic[x] = f(x//2) + f(-(-x//2)) + (x//2) + (-(-x//2))
        return dic[x]

print(f(n))
