
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# This is the recursive version
class Solution1:
    # @param root, a tree node
    # @return a list of integers

    def addNode(self, root, treeNodes):
        if root == None:
            return
        self.addNode(root.left, treeNodes)
        treeNodes.append(root.val)
        self.addNode(root.right, treeNodes)

    def inorderTraversal(self, root):
        TreeNodes = []

        self.addNode(root, TreeNodes)
        return TreeNodes
