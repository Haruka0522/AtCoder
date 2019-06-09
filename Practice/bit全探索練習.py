A = ["orange","banana","apple","strawberry"]
bin_list = []
for i in range(len(A)**2):
    bin_list = [0] * len(A)
    fruits = []
    for j in range(len(A)):
        if i>>j & 1:
            bin_list[j] = 1
            fruits.append(A[j])
    
    #print(bin_list)
    print(fruits)
