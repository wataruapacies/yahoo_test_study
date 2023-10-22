n = int(input())

w = []
x = []

for _ in range(n):
    wi , xi = map(int,input().split())
    w.append(wi)
    x.append(xi)
#print(w)

num = [0]*24
#print(num)
for i in range(24):
    for j in range(n):
        if x[j] <= i and i < x[j] + 9:
            num[i] = num[i] + w[j]
            continue
        if x[j] + 9 > 24:
            if x[j] + 9 - 24 > i:
                num[i] = num[i] + w[j]
                continue

print(max(num))