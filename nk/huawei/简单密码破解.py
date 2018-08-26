while True:
    try:
        a,res=input(),''
        alpha = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}
        for i in a:
            if i.isupper():
                if i!="Z":
                    res+=chr(ord(i.lower())+1)
                else:
                    res+="a"
            elif i.islower():
                for j in alpha.keys():
                    if i in j:
                        res += str(alpha[j])
                        break
            else:
                res += i
        print(res)
    except:
        break