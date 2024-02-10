from collections import deque


n = int(input())

saitan = [10**9] * (n)


# key: ワープ先の番号, value: ワープ元の番号と所要時間のタプル
choice_dict = {}

for i in range(n - 1):
    a, b, x = map(int, input().split())

    # choice b
    if choice_dict.get(x) is None:
        choice_dict[x] = [(i, b), ]
    else:
        choice_dict[x].append((i, b))

    # choice a
    if choice_dict.get(i+1) is None:
        choice_dict[i+1] = [(i, a), ]
    else:
        choice_dict[i+1].append((i, a))

print(choice_dict)

# ゴールから探索
saitan[n-1] = 0
for target in range(n - 1, 0, -1):
    #print(target)
    for origin, time in choice_dict[target]:
        saitan[origin] = min(saitan[origin], saitan[target] + time)

print(saitan)

# だめだ、ワープで戻ることが想定できてない
