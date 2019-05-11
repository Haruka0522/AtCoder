N = int(input())
S = input()
akuse = "b"
akuse_list = ["b"]
for i in range(1,N):
    if(i % 3 == 1):
        akuse = "a" + akuse + "c"
    elif(i % 3 == 2):
        akuse = "c" + akuse + "a"
    else:
        akuse = "b" + akuse + "b"
    akuse_list.append(akuse)

if(S not in akuse_list):
    print(-1)
else:
    print(akuse_list.index(S))
