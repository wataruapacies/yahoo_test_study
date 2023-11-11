n , x = map(int,input().split())

s = list(map(int,input().split()))

count = 0
for i in range(n):
    if s[i] <= x:
        count += s[i]
print(count)