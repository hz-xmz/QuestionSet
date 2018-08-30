# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    s = ''
    str_dict = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.str_dict[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.str_dict:
            self.str_dict[char] += 1
        else:
            self.str_dict[char] = 1

