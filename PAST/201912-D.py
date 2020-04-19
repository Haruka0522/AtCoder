N = int(input())
A_list = [int(input()) for i in range(N)]
A_list.sort()
correct = list(range(1,N+1))
fusoku = set(correct)-set(A_list)
if fusoku == set():
    print("Correct")
else:
    for i in range(N-1):
        if A_list[i] == A_list[i+1]:
            jufuku = A_list[i]
            break
    print(jufuku,list(fusoku)[0])
