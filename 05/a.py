n = int(input())

a = list(map(int,input().split()))

#print(a)

ans = 'Yes'
i = 0
same = a[0]
for b in a:
    if same != b:
        print('No')
        exit()
    i += 1
print('Yes')