n = int(input())
ans = []

i = 1
while i ** 2 <= n:
    if n % i == 0:
        print(i)
        if n // i != i:
            ans.append(n//i)
    i += 1
for i in ans[::-1]:
    print(i)

if i == 1:
    print(1)
