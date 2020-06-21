import collections
def change_dict_key_exist_setdefault(d, old_key, new_key):
    if old_key in d:
        tmp = d[new_key]
        d.setdefault(new_key, d.pop(old_key))
        d[new_key] += tmp
N = int(input())
A_li = list(map(int,input().split()))
ans = sum(A_li)
c = collections.Counter(A_li)
Q = int(input())
for i in range(Q):
    B,C = map(int,input().split())
    ans -= (c[B] * (B-C))
    change_dict_key_exist_setdefault(c,B,C)
    print(ans)
