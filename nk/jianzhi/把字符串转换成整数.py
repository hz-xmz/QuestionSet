# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sym = ['+', '-']
        if s == '':
            return 0
        elif s[0] in sym:
            for i in range(1, len(s)):
                if s[i] not in num:
                    return 0
            res = 0
            for i in range(1, len(s)):
                temp = int(s[i]) * pow(10, len(s) - 1 - i)
                res += temp
            if s[0] == '+':
                return res
            else:
                return 0 - res
        else:
            if len(s) == 1 and s[0] == 0:
                return 0
            for i in range(len(s)):
                if s[i] not in num:
                    return 0
            res = 0
            for i in range(len(s)):
                temp = int(s[i]) * pow(10, len(s) - 1 - i)
                res += temp
            return res
