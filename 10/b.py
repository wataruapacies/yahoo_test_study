b = int(input())



a = 1
while True:
    aa = a ** a
    if aa == b:
        print(a)
        exit()
    else:
        a += 1
        if aa > b:
            break
print("-1")