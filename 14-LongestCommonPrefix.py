class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):


        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        minLength = len(strs[0])
        minIndex = 0
        for i in range(len(strs)):
            if len(strs[i]) < minLength:
                minLength = len(strs[i])
                minIndex = i
        minStr = strs[minIndex]
        IndexCount = [0 for i in range(len(minStr))]

        for i in range(len(minStr)):
            for j in range(len(strs)):
                if strs[j][i] == minStr[i]:
                    IndexCount[i] += 1

        prefix = ''
        for i in range(len(minStr)):
            if IndexCount[i] == len(strs):
                prefix += minStr[i]
            else:
                break
        return prefix
