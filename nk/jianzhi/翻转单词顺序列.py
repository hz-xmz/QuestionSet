# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp = s.split(' ')
        return ' '.join(temp[::-1])    