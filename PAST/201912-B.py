N = int(input())
A_list = [int(input()) for i in range(N)]
for i in range(N-1):
    mae = A_list[i]
    ima = A_list[i+1]
    if ima == mae:
        print("stay")
    elif ima > mae:
        print("up "+str(ima-mae))
    else:
        print("down "+str(mae-ima))

