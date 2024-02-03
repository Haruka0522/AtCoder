from collections import deque
import time

stime = time.time()

n = int(input())
grid = [list(input()) for _ in range(n)]
start_position = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'P':
            grid[i][j] = '.'
            start_position.append([i, j])

Queue = deque()

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

Queue.append((start_position[0][0], start_position[1][0], start_position[0][1], start_position[1][1]))

dist = [[[[-1] * n for _ in range(n)] for __ in range(n)] for ___ in range(n)]
dist[start_position[0][0]][start_position[1][0]][start_position[0][1]][start_position[1][1]] = 0

# bfs
while Queue:
    h1, h2, w1, w2 = Queue.popleft()
    for i in range(4):
        nh1, nh2 = h1 + dh[i], h2 + dh[i]
        nw1, nw2 = w1 + dw[i], w2 + dw[i]
        if 0 <= nh1 < n and 0 <= nw1 < n and grid[nh1][nw1] == '.':
            nh1, nw1 = nh1, nw1
        else:
            nh1, nw1 = h1, w1
        if 0 <= nh2 < n and 0 <= nw2 < n and grid[nh2][nw2] == '.':
            nh2, nw2 = nh2, nw2
        else:
            nh2, nw2 = h2, w2
        if dist[nh1][nh2][nw1][nw2] == -1:
            dist[nh1][nh2][nw1][nw2] = dist[h1][h2][w1][w2] + 1
            Queue.append((nh1, nh2, nw1, nw2))
            if nh1 == nh2 and nw1 == nw2:
                print(dist[nh1][nh2][nw1][nw2])
                exit()

    if time.time() - stime > 3.85:
        print(-1)
        exit()


print(-1)
