def all_zero(lst,num):
    while num < 10:
        if lst[num]!=0:
            return False
        num += 1
    return True

k = int(input())

num = [0] * 10

