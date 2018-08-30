class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None:
            return False
        temp  = []
        for i in numbers:
            if i in temp:
                duplication[0] = i
                return True
            temp.append(i)
        return False

res = ['a']
print(Solution().duplicate([2,3,1,0,2,5,3],res))
print(Solution().duplicate([0,2,5,3],res))