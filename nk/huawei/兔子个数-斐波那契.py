while True:
    try:
        n = int(input())
        lists = [1,1]
        if n == 0 or n == 1:
            print(list[n])
        else:
            for i in range(2,n):
                lists.append(lists[-2] + lists[-1])
        print(lists[-1])
    except:
        break
