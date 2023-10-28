n = input()

n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

#print(n1)

if n1*n2 == n3:
    print(n)
elif n1*n2 < 10 and n1*n2 > n3:
    ans = n1*100 + n2*10 + n1*n2
    print(ans)
elif n1*(n2+1) < 10:
    ans = n1*100 + (n2+1)*10 + n1*(n2+1)
    print(ans)
else:
    ans = (n1+1)*100
    print(ans)