#c = "bbabcbabccc"
#print(c.replace('abc',''))

#print(c)

#idx = c.find("abc")
#print(idx)

#c = c[:idx] + c[idx+3:]
#print(c)

s = input()

while True:
    idx = s.find("ABC")
    #print(idx)
    if idx < 0:
        break
    s = s[:idx] + s[idx+3:]
print(s)


