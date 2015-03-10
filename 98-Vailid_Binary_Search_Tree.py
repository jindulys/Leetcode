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


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def validBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min:
            return False
        if root.val >= max:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)

    def isValidBST(self, root):
        return self.validBST(root, -2147483649, 2147483648)
