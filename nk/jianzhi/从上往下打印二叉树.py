class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        list = []
        start = [root]
        while start:
            temp = start.pop(0)
            list.append(temp.val)
            if temp.left:
                start.append(temp.left)
            if temp.right:
                start.append(temp.right)
        return list