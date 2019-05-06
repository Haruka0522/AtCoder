N = int(input())
ok_flag = 0
jufuku = 0
words = []
word_mae = input()
words.append(word_mae)
for i in range(N-1):
    word_ima = input()
    if(list(word_mae)[-1] == list(word_ima)[0]):
        ok_flag += 1
    if(word_ima in words):
        jufuku = 1
        break
    words.append(word_ima)
    word_mae = word_ima
if(jufuku == 1):
    print("No")
elif(ok_flag == N-1):
    print("Yes")
else:
    print("No")