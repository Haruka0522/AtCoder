a = []
while True:
    try:
        a.append(input())
    except:
        break
a.reverse()
for i in range(len(a)):
    print(a[i])
