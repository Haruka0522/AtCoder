N,A,B = map(int,input().split())
S = list(input())
cnt_a = 0
cnt_b = 0
for i,moji in enumerate(S):
    if moji == "c":
        print("No")
    elif moji == "a":
        if cnt_a < A+B:
            print("Yes")
            cnt_a += 1
        else:
            print("No")
    else:
        if cnt_a < A+B and cnt_b < B:
            print("Yes")
            cnt_a += 1
            cnt_b += 1
        else:
            print("No")
