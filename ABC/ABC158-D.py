S = input()
Q = int(input())
rev = False
for i in range(Q):
    query = input()
    if query == "1":
        T = 1
        rev = not(rev)
    else:
        T,F,C = query.split()
        if rev:
            if F == "1":
                S = S + C
            else:
                S = C + S
        else:
            if F == "1":
                S = C + S
            else:
                S = S + C
if rev:
    print("".join(list(reversed(S))))
else:
    print(S)
