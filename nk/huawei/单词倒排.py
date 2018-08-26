while True:
    try:
        s = input()
        res = ''
        for i in s:
            if i.isalpha():
                res += i
            else:
                res += ' '
        print(' '.join(res.split()[::-1]))
    except:
        break