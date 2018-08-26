class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        left = self.TreeDepth(pRoot.left) + 1
        right = self.TreeDepth(pRoot.right) + 1
        return max(left,right)