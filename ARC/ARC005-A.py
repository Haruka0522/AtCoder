N = int(input())
words = input()[:-1].split()
tkhs = ["TAKAHASHIKUN","Takahashikun","takahashikun"]
ans = 0
for word in words:
    if word in tkhs:
        ans += 1
print(ans)
