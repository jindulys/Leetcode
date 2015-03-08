import copy
from sets import Set
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        n = len(S)
        result = self.getSubsets(S,n)
        return result

    def getSubsets(self,S,n):
        result = []
        if n == 0:
            return []
        for i in xrange(n):
            S_copy = copy.deepcopy(S)
            del S_copy[i]
            tmp = self.getSubsets(S_copy, n-1)
            for t in tmp:
                result.append(t)
        result.append(S)
        return result

if __name__ == '__main__':
    s = Solution()
    myAns = s.subsets([1,2,3,4])
    print myAns
