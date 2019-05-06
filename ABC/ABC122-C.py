'''
TLEが出たコード
a,b = map(int,input().split())
S = list(input())
for i in range(b):
    count = 0
    x,y = map(int,input().split())
    S_a = S[x-1:y]
    #print(S_a)
    for i in range(y-x):
        if(S_a[i]=="A"):
            if(S_a[i+1]=="C"):
                count += 1
    print(count)
'''

'''
もう1パターンTLEがでたこーど
n,q = map(int,input().split())
S = input()
for i in range(q):
    count = 0
    x,y = map(int,input().split())
    S_a = S[x-1:y]
    for j in range(y-x):
        if(S_a[j:j+2]=="AC"):
            count += 1
    print(count)
'''

'''
これもTLE
n,q = map(int,input().split())
S = input()
for i in range(q):
    count = 0
    x,y = map(int,input().split())
    S_a = S[x-1:y]
    for j in range(y-x):
        if(S_a[j]=="A"):
            if(S_a[j+1]=="C"):
                count += 1
    print(count)
'''