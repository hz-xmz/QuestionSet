while True:
    try:
        s = input()
        res, char = [False] * len(s), []
        # 提取英文字母
        for i, v in enumerate(s):
            if v.isalpha():
                char.append(v)
            else:
                res[i] = v
        # 排序
        char.sort(key=lambda c: c.lower())
        # 将char中对应的字符填到res中。
        for i, v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
        print("".join(res))
    except:
        break