total = 0
for i in range(3):
    haiten,wariai = map(int,input().split())
    tokuten = haiten*wariai/10
    total += tokuten
print(int(total))