import numpy as np
tmp = [
    [list("###"),
     list("#.#"),
     list("#.#"),
     list("#.#"),
     list("###")],
    [list(".#."),
     list("##."),
     list(".#."),
     list(".#."),
     list("###")],
    [list("###"),
     list("..#"),
     list("###"),
     list("#.."),
     list("###")],
    [list("###"),
     list("..#"),
     list("###"),
     list("..#"),
     list("###")],
    [list("#.#"),
     list("#.#"),
     list("###"),
     list("..#"),
     list("..#")],
    [list("###"),
     list("#.."),
     list("###"),
     list("..#"),
     list("###")],
    [list("###"),
     list("#.."),
     list("###"),
     list("#.#"),
     list("###")],
    [list("###"),
     list("..#"),
     list("..#"),
     list("..#"),
     list("..#")],
    [list("###"),
     list("#.#"),
     list("###"),
     list("#.#"),
     list("###")],
    [list("###"),
     list("#.#"),
     list("###"),
     list("..#"),
     list("###")]]

N = int(input())
ans = []
inp = np.array([list(input()) for _ in range(5)])
for i in range(1, 4*N+1, 4):
    ans.append(str(tmp.index(inp[:, i:i+3].tolist())))
print("".join(ans))
