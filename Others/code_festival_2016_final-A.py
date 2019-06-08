H,W = map(int,input().split())
for i in range(H):
    S = input().split()
    if "snuke" in S:
        gyou = S.index("snuke")
        retsu = i + 1
gyou = chr(gyou+65)
print(gyou+str(retsu))
        
