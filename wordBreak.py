class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        # use back check

        # build an array A [False] * n
        # from n-1 to 0

        # A[i] == true if (1) s[i:n] in dict  (2) exist j, j>i, where A[j] == true and s[i:j] in dict

        n = len(s)
        wordArray = [False]*n

        i = n-1
        while i >= 0:
            if s[i:n] in dict:
                wordArray[i] = True

            else:
                for j in range(i+1,n):
                    if wordArray[j] and s[i:j] in dict:
                        wordArray[i] = True
                        break
            i = i -1
        return wordArray[0]
