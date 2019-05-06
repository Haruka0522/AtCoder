S = input()
K = int(input())
bubunmojiretsu = []
if (len(S) < K):
    print(0)
else:
    for i in range(len(S)-(K-1)):
        bubunmojiretsu.append(S[i:i + K])
    print(len(set(bubunmojiretsu)))
