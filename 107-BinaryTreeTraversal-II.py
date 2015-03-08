# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):

        def _processNode(toProcess):
            nextLevel = []
            vals = []

            if len(toProcess) == 0:
                return
            for n in toProcess:
                vals.append(n.val)
                if n.left != None:
                    nextLevel.append(n.left)
                if n.right != None:
                    nextLevel.append(n.right)

            _processNode(nextLevel)
            solution.append(vals)



        solution = []
        if root == None:
            return solution

        toProcess = [root]
        _processNode(toProcess)
        return solution
