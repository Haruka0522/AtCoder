A,B,K = map(int,input().split())
"""
for i in range(K):
    if(A >= 1):
        A -= 1
    elif(B >= 1):
        B -= 1
    else:
        continue
"""

"""
if K >= A:
    _A = 0
else:
   _A = A - K

if K-A >= 1:
    _B = B-(K-A)
print(_A,_B)
"""

if K <= A:
    A_ = A - K
    B_ = B
elif K >= A + B:
    A_ = 0
    B_ = 0
else:
    A_ = 0
    B_ = B - (K - A)
print(A_,B_)
