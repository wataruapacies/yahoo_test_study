from collections import deque
h , w = map(int,input().split())
s = [list(input()) for l in range(h)]

#print(s)
#print(s[1][3])

sens = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            sens.append([i,j])
#print(sens[1][1])

#print(len(sens))
friend = [[] for _ in range(len(sens))]
for i in range(len(sens)):
    for j in range(len(sens)):
        if i == j:
            continue
        if max(abs(sens[i][0]-sens[j][0]),abs(sens[i][1]-sens[j][1])) == 1:
            friend[i].append(j)
#print(friend)

q = [-1] * len(sens)

if len(sens) == 0:
    print("0")
    exit()

que = deque()
que.append(0)
q[0] = 0
g_n = 1
while True:
    #print(q)
    if min(q)==0:
        break
    if len(que)==0:
        for i in range(len(sens)):
            if q[i] == -1:
                que.append(i)
                g_n = g_n + 1
                q[i] = 0
                break
    now = que.popleft()
    #print(que)
    for i in range(len(friend[now])):
        if q[friend[now][i]]==-1:
            que.append(friend[now][i])
            q[friend[now][i]] = 0
print(g_n)
    