S = list(input())
T = int(input())
now = [0,0]
hatena = 0
for ope in S:
    if ope == "L":
        now[0] -= 1
    elif ope == "R":
        now[0] += 1
    elif ope == "U":
        now[1] += 1
    elif ope == "D":
        now[1] -= 1
    else:
        hatena += 1
if T == 1:
    print(abs(now[0])+abs(now[1])+hatena)
