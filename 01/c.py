n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [list(input()) for _ in range(n)]

score_arr = [0 for _ in range(n)]
q_arr = [[] for _ in range(n)]

for i in range(n):
    score_arr[i] += i+1
    for j in range(m):
        if s[i][j] == 'o':
            score_arr[i] += a[j]
        else:
            q_arr[i].append(a[j])
# print(score_arr)
# print(q_arr)

for i in range(n):
    score = score_arr[i]
    arr = sorted(q_arr[i], reverse=True)
    rival_arr = sorted(score_arr, reverse=True)
    num = 0
    for j in range(len(arr)):
        if score >= rival_arr[0]:
            break
        else:
            score += arr[j]
            num += 1
    print(num)