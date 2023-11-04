num_9 = [i+1 for i in range(9)]

def compare(mp):
    #print(a)
    np=sorted(mp)
    #print(np)
    #print(num_9)
    if np == num_9:
        return True
    else:
        return False


if __name__ == "__main__":
    a = [list(map(int,input().split())) for i in range(9)]
    #print(a[1][1])
    
    b = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        tmp = a[i]
        #print("No.1",tmp)
        if compare(tmp):
            for j in range(9):
                if i == 1 or i == 4 or i == 7:
                    if j == 1 or j == 4 or j == 7:
                        tmp = [a[i-1][j-1],a[i][j-1],a[i+1][j-1],a[i-1][j],a[i][j],a[i+1][j],a[i-1][j+1],a[i][j+1],a[i+1][j+1]]
                        #print("No.2",tmp," i=",i," j=",j)
                        #print(a[i][j])
                        if compare(tmp):
                            pass
                        else:
                            print('No')
                            exit()
                b[j][i] = a[i][j]
                if i == 8:
                    tmp = b[j]
                    #print("No.3",tmp)
                    if compare(tmp):
                        pass
                    else:
                        print('No')
                        exit()
        else:
            print('No')
            exit()
    #print(b)
    print("Yes")