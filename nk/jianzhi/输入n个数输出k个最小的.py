while True:
    try:
        n,k = map(int,input().split())
        nums = [int(i) for i in input().split()]
        res = sorted(nums)
        ans = ''
        for i in range(k):
            ans += str(res[i])
            ans += ' '
        print(ans[:-1])
    except:
        break
