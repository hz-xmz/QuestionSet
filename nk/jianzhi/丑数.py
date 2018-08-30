# 不能完全通过
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         if index <= 0:
#             return 0
#         ugly = []
#         for n in range(1,10000):
#             temp = n
#             for i in [2, 3, 5]:
#                 while n % i == 0:
#                     n = n / i
#             if n == 1:
#                 ugly.append(temp)
#         return ugly[index-1]

class Solution:
    def GetUglyNumber_Solution(self, index):
        if (index <= 0):
            return 0
        ugly = [1]
        two = 0
        three = 0
        five = 0
        for i in range(1,index):
            newUgly = min(ugly[two]*2, ugly[three]*3, ugly[five]*5)
            ugly.append(newUgly)
            if (newUgly % 2 == 0):
                two += 1
            if (newUgly % 3 == 0):
                three += 1
            if (newUgly % 5 == 0):
                five += 1
        # print(ugly)
        return ugly[-1]

print(Solution().GetUglyNumber_Solution(7))