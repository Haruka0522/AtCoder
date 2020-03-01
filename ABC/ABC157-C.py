N,M = map(int,input().split())
ichi = []
juu = []
hyaku = []
for i in range(M):
    if N == 1:
        s,c = map(int,input().split())
        ichi.append(c)
    elif N == 2:
        s,c = map(int,input().split())
        if s == 1:
            juu.append(c)
        else:
            ichi.append(c)
    elif N == 3:
        s,c = map(int,input().split())
        if s == 1:
            hyaku.append(c)
        elif s == 2:
            juu.append(c)
        else:
            ichi.append(c)
ichi = set(ichi)
juu = set(juu)
hyaku = set(hyaku)
if N == 1:
    if len(ichi) >= 2:
        print(-1)
    else:
        print(min(ichi))
elif N == 2:
    if juu == set([0]):
        print(-1)
    elif len(juu) >= 2:
        print(-1)
    elif len(ichi) >= 2:
        print(-1)
    else:
        if ichi == set():
            ichi.add(0)
        if juu == set():
            juu.add(1)
        print(str(min(juu))+str(min(ichi)))
else:
    if hyaku == set([0]):
        print(-1)
    elif len(hyaku) >= 2:
        print(-1)
    elif len(juu) >= 2:
        print(-1)
    elif len(ichi) >= 2:
        print(-1)
    else:
        if hyaku == set():
            hyaku.add(1)
        if juu == set():
            juu.add(0)
        if ichi == set():
            ichi.add(0)
        print(str(min(hyaku))+str(min(juu))+str(min(ichi)))

