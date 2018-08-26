import re
import sys
a = []
str = sys.stdin.readline().strip()
while str != "":
    a.append(str)
    str = sys.stdin.readline().strip()
try:
    for s in a:
        # a = re.findall(r'(.{3,}).*\1', s) #匹配字符串中是否存在长度为3的子串
        b1 = re.findall(r'\d', s)  #数字
        b2 = re.findall(r'[A-Z]', s) #大写字母
        b3 = re.findall(r'[a-z]', s) #小写字母
        b4 = re.findall(r'[^0-9A-Za-z]', s)
        # print('OK') if ([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(s) > 8) else print('NG')
        if [b1, b2, b3, b4].count([]) <= 1 and len(s) > 8:
            res = 0
            for j in range(len(s) - 3):
                for k in range(j + 3, len(s) - 3):
                    if s[j] == s[k] and s[j + 1] == s[k + 1] and s[k + 2] == s[k + 2]:
                        res = 1
            if res:
                print("NG")
            else:
                print("OK")
        else:
            print('NG')
except:
    pass