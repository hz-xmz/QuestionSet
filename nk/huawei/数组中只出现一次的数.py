# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        for i in array:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res

print(Solution().FindNumsAppearOnce([1,2,2,1,4,5,6,4]))