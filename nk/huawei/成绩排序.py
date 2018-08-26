while True:
    try:
        n = int(input())
        f = int(input())
        res = []
        for i in range(n):
            s = input().split()
            s[1] = int(s[1])
            res.append(s)
        if f == 0:
           res = sorted(res, key=lambda x: x[1],reverse =True)
        else:
            res = sorted(res, key=lambda x: x[1])
        for i in res:
            print(i[0],i[1])
    except:
        break