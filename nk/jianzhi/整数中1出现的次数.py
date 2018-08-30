# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        temp = []
        for i in range(1,n+1):
            if '1' in str(i):
                temp.append(str(i))
        return ''.join(temp).count('1')

print(Solution().NumberOf1Between1AndN_Solution(13))