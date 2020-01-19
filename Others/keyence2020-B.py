N = int(input())
x_list = []
l_list = []
for i in range(N):
    x,l = map(int,input().split())
    x_list.append(x)
    l_list.append(l)
total_ugokuhani = 2*sum(l_list)
limit_ugokuhani = x_list[-1]+l_list[-1] - x_list[0]-l_list[0]
remove_robot = 0
while(True):
    if total_ugokuhani <= limit_ugokuhani:
        break
    total_ugokuhani -= 2*(min(l_list))
    del l_list[l_list.index(min(l_list))]
    remove_robot += 1
print(N-remove_robot)
