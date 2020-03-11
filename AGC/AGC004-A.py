ABC = list(map(int,input().split()))
ABC.sort()
mid = ABC[-1] // 2
print(abs(ABC[0] * ABC[1] * mid - ABC[0] * ABC[1] * (ABC[2]-mid)))
