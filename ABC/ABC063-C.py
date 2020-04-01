N = int(input())
score_li = [int(input()) for i in range(N)]
score = sum(score_li)
if score % 10 != 0:
    print(score)
    exit()
else:
    score_li.sort()
    for i in score_li:
        if i % 10 != 0:
            print(score - i)
            exit()
print(0)
