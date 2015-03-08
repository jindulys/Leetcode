# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        level = 0
        q = deque()
        q.append((root,level))
        result = []
        currentLevelNodes = []
        while len(q) != 0:
            currentNode, currentLevel = q.popleft()
            if currentLevel > level:
                result.append(currentLevelNodes)
                currentLevelNodes = []
                level = level + 1
            currentLevelNodes.append(currentNode.val)
            if currentNode.left != None:
                q.append((currentNode.left, currentLevel + 1))
            if currentNode.right != None:
                q.append((currentNode.right, currentLevel + 1))


        # note: add the last elements in currentLevelNodes
        result.append(currentLevelNodes)
        return result



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        solution = []

        if root == None:
            return solution

        toProcess = [root]

        while len(toProcess) != 0:
            vals = []
            nextLevel = []
            for n in toProcess:
                vals.append(n.val)
                if n.left != None:
                    nextLevel.append(n.left)
                if n.right != None:
                    nextLevel.append(n.right)
            solution.append(vals)
            toProcess = nextLevel
        return solution
