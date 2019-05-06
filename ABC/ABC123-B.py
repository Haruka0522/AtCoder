li = [int(input()) for i in range(5)]
li_amari = []
time = 0
for i in li:
    if (i % 10 == 0):
        li_amari.append(0)
    else:
        li_amari.append(10 - (int(i % 10)))

a = li_amari.index(max(li_amari))

max_li = li[a]

del li[a]
del li_amari[a]

for j in range(4):
    time += (li[j]+li_amari[j])

print(time + max_li)
