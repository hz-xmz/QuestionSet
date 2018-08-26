while True:
    try:
        need, decode = input(), input()
        res1, res2 = "", ""
        # 加密
        for i in need:
            if i.isupper():
                if i != "Z":
                    res1 += chr(ord(i) + 1).lower()
                else:
                    res1 += "a"
            elif i.islower():
                if i != "z":
                    res1 += chr(ord(i) + 1).upper()
                else:
                    res1 += "A"
            elif i.isdigit():
                res1 += chr(ord(i) + 1)
            else:
                res1 += "0"
        # 解密
        for j in decode:
            if j.isupper():
                if j != "A":
                    res2 += chr(ord(j) - 1).lower()
                else:
                    res2 += "z"
            elif j.islower():
                if j != "a":
                    res2 += chr(ord(j) - 1).upper()
                else:
                    res2 += "Z"
            elif j.isdigit():
                res2 += chr(ord(i) - 1)
            else:
                res2 += "9"
        print(res1)
        print(res2)
    except:
        break