class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        temp = 0
        res = max(array)
        print(res)
        for i in array:
            temp = max(i,temp+i)
            res = max(res,temp)
        return res

if __name__ == '__main__':
    array = [6,-3,-2,7,-15,1,2,2]
    print(Solution().FindGreatestSumOfSubArray(array))