card = []
a,b,c = map(int,input().split())
card.append(a)
card.append(b)
card.append(c)
a,b,c = map(int,input().split())
card.append(a)
card.append(b)
card.append(c)
a,b,c = map(int,input().split())
card.append(a)
card.append(b)
card.append(c)
N = int(input())
for i in range(N):
    b = int(input())
    try:
        card[card.index(b)] = -1
    except:
        continue
if card[0] == card[1] == card[2] or card[3] == card[4] == card[5] or card[6] == card[7] == card[8] or card[0] == card[3] == card[6] or card[1] == card[4] == card[7] or card[2] == card[5] == card[8] or card[0] == card[4] == card[8] or card[2] == card[4] == card[6]:
    print("Yes")
else:
    print('No')
