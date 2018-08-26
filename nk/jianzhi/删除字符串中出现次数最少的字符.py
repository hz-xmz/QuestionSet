
while True:
    try:
        s = input()
        char = {}
        for i in s:
            if i not in char.keys():
                char[i] = 1
            else:
                char[i] += 1
        for j in char:
            if char[j] == min(char.values()):
                s = s.replace(j, "")
        print(s)
    except:
        break