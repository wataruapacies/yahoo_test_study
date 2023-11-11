s = input()


while True:
    s1 = s.replace("ABC","")
    if s1 == s:
        break
    s = s1
print(s)