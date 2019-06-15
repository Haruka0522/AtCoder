A,B,C = map(int,input().split())
ans = 0
while(True):
    if A == B == C:
        print(0)
        exit()

    if abs(A-B)<2 or abs(B-C)<2 or abs(C-A)<2:
        if A > B and A > C:
            B += 1
            C += 1
        elif B > C and B > A:
            C += 1
            A += 1
        else:
            A += 1
            B += 1
    else:
        if A == B:
            C += 2
        elif B == C:
            A += 2
        elif C == A:
            B += 2


    if A == B == C:
        print(ans)
        exit()

    ans += 1
