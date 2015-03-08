class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):

        stack = []
        res = ''
        i = 0
        while i < len(path):

            end = i+1
            while end < len(path) and path[end] != '/':
                end += 1
            currentPath = path[i+1:end]

            if len(currentPath) != 0:
                if currentPath == '..':
                    if len(stack) != 0: stack.pop()
                elif currentPath != '.':
                    stack.append(currentPath)

            i = end
        if stack == []: return '/'
        for i in stack:
            res += '/' + i
        return res
