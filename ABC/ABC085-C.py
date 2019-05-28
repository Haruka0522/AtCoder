N,Y = map(int,input().split())
for yukichi in range(int(Y/10000)+1):
        for ichiyo in range(int(Y/5000)+1):
            hideyo = N-yukichi-ichiyo
            if(10000*yukichi+5000*ichiyo+1000*hideyo == Y and hideyo >= 0):
                print(yukichi,ichiyo,hideyo)
                exit()
print("-1 -1 -1")
