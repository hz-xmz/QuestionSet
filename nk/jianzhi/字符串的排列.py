import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == '' or ss is None:
            return []
        temp = list(itertools.permutations(list(ss),len(ss)))
        print(temp)
        for i in range(len(temp)):
            temp[i] = ''.join(temp[i])
        res = list(set(temp))
        return sorted(res)

print(Solution().Permutation(['a','b','c']))