'''
X = int(input())
able = []
for i in range(100,105+1):
    able.append(i)
for i in range(200,210+1):
    able.append(i)
for i in range(300,315+1):
    able.append(i)
for i in range(400,420+1):
    able.append(i)
for i in range(500,525+1):
    able.append(i)
for i in range(600,630+1):
    able.append(i)
if X >= 630:
    print(1)
    exit()
elif X in able:
        print(1)
        exit()
print(0)
'''


'''
X = int(input())
able = list()
if X >= 700:
    print(1)
    exit()
else:
    for i in range(1,7+1):
        for j in range(100*i,105*i+1):
            able.append(j)
            if X in able:
                print(1)
                exit()
print(0)
'''
