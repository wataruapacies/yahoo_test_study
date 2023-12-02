n , s , m , l = map(int,input().split())

dic = {6 : s / 6 , 8 : m / 8 , 12 : l / 12}

#print(dic)
#print(min(dic, key=dic.get))

dic2 = sorted(dic.items(), key=lambda x:x[1])

ans = []

#ans.append(s*(n//6+1))
p = s*(n//6)
q = n%6
if q != 0:
    p += s
ans.append(p)

#ans.append(m*(n//8+1))
p = m*(n//8)
q = n%8
if q != 0:
    p += m
ans.append(p)


#ans.append(l*(n//12+1))
p = l*(n//12)
q = n%12
if q != 0:
    p += l
ans.append(p)




#ans.append(l*(n//12)+m*((n%12)//8)+s*(((n%12)%8)//6+1))
p = l*(n//12)+m*((n%12)//8)+s*(((n%12)%8)//6)
q = ((n%12)%8)%6
if q != 0:
    p += s
ans.append(p)

#ans.append(l*(n//12)+s*((n%12)//6+1))
p = l*(n//12)+s*((n%12)//6)
q = (n%12)%6
if q != 0:
    p += s
ans.append(p)



#ans.append(l*(n//12)+m*((n%12)//8+1))
p = l*(n//12)+m*((n%12)//8)
q = (n%12)%8
if q != 0:
    p += m
ans.append(p)


#ans.append(m*(n//8)+s*((n%8)//6+1))
p = m*(n//8)+s*((n%8)//6)
q = (n%8)%6
if q != 0:
    p += s
ans.append(p)
print(min(ans))