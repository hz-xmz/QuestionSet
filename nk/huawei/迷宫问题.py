
try:
    # a,b=[int(i) for i in input().split()]
    # m=[]
    # for i in range(a):
    #     m.append([int(i) for i in input().split()])
    a,b = 5,5
    m = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
    i,j = 0,0
    lu = [(i,j)]
    while i != a-1 or j != b-1:
        if i<a-1 and m[i+1][j] == 0:
            i += 1
            lu.append((i,j))
        elif j<b-1 and m[i][j+1] == 0:
            j += 1
            lu.append((i,j))
    print(lu)
    # for i in lu:
    #     print('(%d,%d)' % (i[0], i[1]))
except:
    pass

