N = int(input())
correct_sum = 0
ans = list()
for i in range(1,10):
    for j in range(1,10):
        correct_sum += (i * j)
difference = correct_sum - N
for i in range(1,10):
    for j in range(1,10):
        if i * j == difference:
            ans.append([str(i),str(j)])
for i in ans:
    print(" x ".join(i))
