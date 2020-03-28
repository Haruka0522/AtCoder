C,c = input().split()
small = [chr(i) for i in range(97,97+26)]
capital = [chr(i) for i in range(65,65+26)]
if small.index(c) == capital.index(C):
    print("Yes")
else:
    print("No")
