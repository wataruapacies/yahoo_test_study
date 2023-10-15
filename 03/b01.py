n ,m = map(int,input().split())

s = input()
t = input()

atama = t[0:n]
oshiri = t[-n:]

if s == atama:
    if s == oshiri:
        print('0')
    else:
        print('1')
else:
    if s == oshiri:
        print('2')
    else:
        print('3')