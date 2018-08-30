# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s is None or s == '':
            return False
        temp = re.match(r'[\+-]?[0-9]*(\.[0-9]*)?([eE][\+-]?[0-9]+)?',s)
        if temp.group(0) == s:
            return True
        else:
            return False