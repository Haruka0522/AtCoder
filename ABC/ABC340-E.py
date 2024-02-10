n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
for i in range(m):
    b_i = b_list[i]
    hand = a_list[b_i]
    a_list[b_i] = 0

    # これは遅いのでだめ
    c = 0
    while hand >= 1:
        c += 1
        hand -= 1
        a_list[(b_i + c) % n] += 1

print(a_list)
