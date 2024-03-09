T = input()
N = int(input())
bags = []
for i in range(N):
    q = list(input().split())
    bags.append(q[1:]+["", ])

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = min(result[key], value)
        else:
            result[key] = value
    return result

kouhos = {"": 0}
for bag in bags:
    for j in bag:
        if j != "":
            tuika_kouho = {}
            for kouho in kouhos.keys():
                if T.startswith(kouho+j):
                    if kouho+j in tuika_kouho:
                        tuika_kouho[kouho+j] = min(kouhos[kouho]+1, tuika_kouho[kouho+j])
                    else:
                        tuika_kouho[kouho+j] = kouhos[kouho]+1
            kouhos = merge_dicts(kouhos, tuika_kouho)
print(kouhos.get(T, -1))
