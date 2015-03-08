class Solution1:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):

        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(needle) == 0:
            return 0


        for i in range(len(haystack) - len(needle) + 1):

            start = 0
            while start < len(needle):
                if haystack[i + start] == needle[start]:
                    start += 1
                else:
                    break
            if start == len(needle):
                return i

        return -1

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):

        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        m = 0
        i = 0
        T = self.getPrefix(needle)
        while m + i < len(haystack):
            if haystack[m+i] == needle[i]:
                if i == len(needle) - 1:
                    return m
                else:
                    i += 1
            else:

                if T[i] > -1:
                    m = m + i - T[i]
                    i = T[i]
                else:
                    i = 0
                    m = m+1
        return -1


    def getPrefix(self, pattern):

        T =[-1] * len(pattern)

        if len(pattern) < 2:
            return T

        T[1] = 0

        pos = 2
        cnt = 0 # next candidate character index

        while pos < len(pattern):

            if pattern[cnt] == pattern[pos-1]:
                cnt += 1
                T[pos] = cnt
                pos += 1
            elif cnt > 0:
                cnt = T[cnt]
            else:
                T[pos] = cnt
                pos += 1
        return T

def test():
    s = Solution()
    print s.strStr("ABCDAB","CDA")
    print s.getPrefix("ABCDABD")

if __name__ == "__main__":
    test()
