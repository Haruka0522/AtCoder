ans_li=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    ans_li.append(a+b)
print(max(ans_li))
