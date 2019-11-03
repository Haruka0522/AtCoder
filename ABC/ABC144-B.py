N = int(input())
kuku_list = []
for i in range(1,10):
    for j in range(1,10):
        kuku_list.append(i*j)
if N in kuku_list:
    print("Yes")
else:
    print("No")
