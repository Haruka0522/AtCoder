N = int(input())
H_list = list(map(int,input().split()))
if N==1:
    print("Yes")
    exit()
'''WA提出
if H_list[0] <= H_list[-1] and min(H_list[1:-1])>= H_list[0] and min(H_list[1:-1])<=H_list[-1] and max(H_list[1:-1])-min(H_list[1:-1]) < 2:
    print("Yes")
else:
   print("No")
'''
for i in range(N-1):
    if H_list[i] < H_list[i+1]:
        H_list[i+1] = H_list[i+1] - 1
if H_list == sorted(H_list):
    print("Yes")
else:
    print("No")
