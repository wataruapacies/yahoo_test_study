n = int(input())

d = list(map(int,input().split()))

count = 0
for i in range(n):#i = 0から
    if i + 1 < 10:
        for j in range(d[i]):
            if i + 1 == j + 1 or (i + 1) * 11 == j + 1:
                count += 1
    elif (i + 1) % 11 == 0:
        for j in range(d[i]):
            if i + 1 == j + 1 or i + 1 == (j + 1) * 11:
                count += 1
print(count)