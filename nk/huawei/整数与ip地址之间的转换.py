while True:
    try:
        ip = input().split('.')
        res = ''
        for i in ip:
            temp = bin(int(i)).replace('0b','')
            while len(temp)<8:
                temp = '0' + temp
            res += temp

        s,a = int(input()),[]
        s = bin(s).replace('0b','')
        while len(s)<32:
            s = '0' + s
        for j in range(4):
            a.append(str(int(s[8*j:8*(j+1)],2)))

        print(int(res, 2))
        print('.'.join(a))

    except:
        break