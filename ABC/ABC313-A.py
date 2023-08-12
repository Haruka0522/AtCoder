n = int(input())
p_list = list(map(int, input().split(" ")))
if n == 1:
    print(0)
else:
    print(max(0, max(p_list[1:])+1-p_list[0]))
