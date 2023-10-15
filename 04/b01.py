n, x = map(int,input().split())

a = list(map(int,input().split()))

#print(a)

a = sorted(a)

num = sum(a)
if num - a[n-2] == x:
    print('0')
elif num - a[0] == x:
    print(a[n-2])
else:
    if (x- (num -a[0] -a[n-2])) <= a[n-2] and (x- (num -a[0] -a[n-2])) >= a[0]:
        print(x- (num -a[0] -a[n-2]))
    else:
        print('-1')