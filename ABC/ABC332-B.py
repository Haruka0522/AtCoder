k,g,m = map(int,input().split())
M = 0
G = 0
for i in range(k):
    if G == g:
        G = 0
    elif M == 0:
        M = m
    else:
        hairu_g = g - G
        daseru_m = M
        if hairu_g >= daseru_m:
            G += daseru_m
            M = 0
        else:
            G += hairu_g
            M -= hairu_g

print(G, M)
