class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def max_Depth(self, root: TreeNode)-> int:
        if not root:
            return 0
        left = self.max_Depth(root.left)
        right = self.max_Depth(root.right)

        return max(left, right)+1
    print(max_Depth([3,9,20,null,null,15,7]))

