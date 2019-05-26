N = int(input())
city_list = []
score_list = []
for i in range(N):
    city,score = input().split()
    score = int(score)
    city_list.append(city)
    score_list.append(score)
city_sort = sorted(city_list)
for i in sorted(list(set(city_list))):
    if(city_list.count(i) == 1):
        print(score_list.index(score_list[city_list.index(i)])+1)
    else:
        list_a = []
        len_same_city = city_list.count(i)
        for j in range(len_same_city):
            list_a.append(score_list[city_list.index(i)])
            city_list[city_list.index(i)] = -1
        list_a = sorted(list_a,reverse=True)
        for k in list_a:
            print(score_list.index(k)+1)
