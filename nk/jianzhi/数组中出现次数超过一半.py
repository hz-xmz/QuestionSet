import collections
try:
    numbers = [1,2,2,2,2,2,3,4,5]
    res = collections.Counter(numbers)
    print(res)
    half = len(numbers)/2
    for i in numbers:
        if i not in res.keys():
            res[i] = 1
        else:
            res[i] += 1
    print(res)
    for k in res.keys():
        if res[k] > half:
            print(k)

    print('0')
except:
    pass
