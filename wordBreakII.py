class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):

        # Step1 generate a list contains all valid pathes

        # an array stores all the valid locs for an index

        # running time O(n^2), space O(n)

        n = len(s)
        validLocs = [None]*n
        i = n - 1

        while i >= 0:
            if s[i:n] in dict:
                validLocs[i] = [n]
            else:
                validLocs[i] = []

            for j in range(i+1,n):
                if s[i:j] in dict and validLocs[j]:
                    validLocs[i].append(j)
            i = i-1


        # Step2 generate the result, basically use a BFS in the graph
        # running time O(M*N) where M is the number of nodes
        result = []
        pathList = [[0]]

        while pathList:
            newPaths = []

            for path in pathList:
                if path[-1] == n:
                    # get the result for this path
                    sentence = [s[path[i]:path[i+1]] for i in xrange(len(path) -1)]
                    result.append(" ".join(sentence))
                else:
                    for nextIndex in validLocs[path[-1]]:
                        newPaths.append(path + [nextIndex])
            pathList = newPaths
        return result
