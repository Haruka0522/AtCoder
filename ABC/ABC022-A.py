N,S,T = map(int,input().split())
W = int(input())
count = 0
for i in range(N-1):
    if(i==0):
        X = W
        if(S <= X and X <= T):
            count += 1
    henkaryou = int(input())
    sonohino_taiju = X + henkaryou
    if(S <= sonohino_taiju and sonohino_taiju <= T):
        count += 1
    X = sonohino_taiju
print(count)