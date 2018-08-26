class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        for i, v in enumerate(array):
            if tsum-v in array[i+1:]:
                res.append([v, tsum-v])
        if res:
            return res[0]
        else:
            return res

print(Solution().FindNumbersWithSum([4,4,5,6],8))