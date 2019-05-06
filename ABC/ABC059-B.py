# リストを使った遊び
'''
ab = [int(input()) for i in range(2)]
if (ab[0] > ab[1]):
    print("GREATER")
elif (ab[0] < ab[1]):
    print("LESS")
else:
    print("EQUAL")
'''

# 普通のやり方
a, b = int(input()), int(input())
if (a > b):
    print("GREATER")
elif (a < b):
    print("LESS")
else:
    print("EQUAL")
