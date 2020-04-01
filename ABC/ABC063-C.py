N = int(input())
score_li = [int(input()) for i in range(N)]
ans = 0
bin_list = []
for i in range(N**2):
    bin_list = [0] * N
    scores = []
    for j in range(N):
        if i>>j & 1:
            bin_list[j] = 1
            scores.append(score_li[j])
    score = sum(scores)
    if score % 10 == 0:
        score = 0
    ans = max(ans,score)
print(ans)
