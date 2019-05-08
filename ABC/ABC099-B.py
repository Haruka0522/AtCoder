'''TLE回答
a,b = map(int,input().split())
tower = [1]
tower_kai = []
for i in range(2,999):
    tower.append(tower[i-2]+i)
for i in range(len(tower)-1):
    tower_kai.append([tower[i],tower[i+1]])
i = 0
while(True):
    ab_list = [a+i,b+i]
    if(ab_list in tower_kai):
        print(i)
        exit()
    i+=1
'''


'''これでもTLE
a,b = map(int,input().split())
tower_list = [[1,3]]
for i in range(3,999):
    tower_list.append([tower_list[i-3][1],tower_list[i-3][1]+i])
i=0
while(True):
    ab_list = [a+i,b+i]
    if(ab_list in tower_list):
        print(i)
        exit()
    i += 1
'''


#'''解答をみて
a,b = map(int,input().split())
print(int((b-a)*(b-a+1)/2-b))
