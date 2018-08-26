while True:
    try:
        m = int(input())
        n = int(input())
        k = int(input())
        matrix1 = []
        matrix2 = []
        res = []
        def muti(s1, s2):
            add = 0
            for j in range(len(s1)):
                add += s1[j] * s2[j]
            return add


        for i in range(m):
            line = input().split()
            line = [int(x) for x in line]
            matrix1.append(line)
        for i in range(n):
            line = input().split()
            line = [int(x) for x in line]
            matrix2.append(line)
        for i in range(k):
            raw = []
            for j in range(n):
                raw.append(matrix2[j][i])
            res.append(raw)

        out = []
        for i in range(m):
            raw = []
            for j in range(k - 1):
                print(muti(matrix1[i], res[j]), end=' ')
            print(muti(matrix1[i], res[-1]))
    except:
        break