# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# this solution is not work for example: {10, 3,15, #,#, 6, 20}
class Solution1:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None:
            return True

        if root.left:
            if root.left.val >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
