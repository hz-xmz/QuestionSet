def fun(res, num):
    if len(num) == 1:
        if num[0] == res:
            return 1
        else:
            return 0
    for i in range(len(num)):
        a = num[i]
        b = num[:]
        b.pop(i)
        if (fun(res - a, b)) or fun(res * a, b) or fun(res / a, b) or fun(res + a, b):
            return 1


while True:
    try:
        num = [float(i) for i in input().split()]

        if fun(24.0, num):
            print('true')
        else:
            print('false')
    except:
        break
