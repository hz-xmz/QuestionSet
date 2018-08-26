while True:
    try:
        str,str_list,res = input(),[],''
        for i in str:
            str_list.append(i)
        temp = sorted(str_list)
        for j in temp:
            res += j
        print(res)
    except:
        break

