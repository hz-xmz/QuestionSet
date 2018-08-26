class Solution:
    # 判断二叉树是否为平衡二叉树
    # 先判断该节点是否平衡
    # 再递归去判断左节点和右节点是否平衡

    # 递归求当前节点的深度
    def TreeDepth(self, node):
        # write code here
        if node is None:
            return 1
        left = self.TreeDepth(node.left) + 1
        right = self.TreeDepth(node.right) + 1
        return max(left, right)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return 1
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            return 0
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
