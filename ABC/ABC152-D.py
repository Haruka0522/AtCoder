N = int(input())
A_list = []
for num in range(1,10):
    i = 1
    while(True):
        A = int(str(num)*i)
        if A > N:
            break
        A_list.append(A)
        i += 1
print(A_list)
