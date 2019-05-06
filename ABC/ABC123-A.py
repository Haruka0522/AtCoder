li = [int(input()) for i in range(5)]
k = int(input())
for i in range(4):
    if (max(li)-min(li) > k):
        print(":(")
        exit()
print("Yay!")
