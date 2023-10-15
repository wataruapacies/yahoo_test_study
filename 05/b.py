n = int(input())

while True:
    if n == 1:
        print('Yes')
        exit()
    if n % 3 == 0:
        n = n / 3
    else:
        break
while True:
    if n == 1:
        print('Yes')
        exit()
    if n % 2 == 0:
        n = n / 2
    else:
        break
print('No')