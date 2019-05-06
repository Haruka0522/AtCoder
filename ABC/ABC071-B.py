abc_list = [chr(i) for i in range(97,97+26)]
input_list = list(input())
p_flag = 0
for i in abc_list:
    try:
        input_list.remove(i)
    except:
        print(i)
        p_flag = 1
        break
if(p_flag == 0):
    print("None")