class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):

        n = len(digits)

        result = [0]*(n+1)

        toAdd = [0]*n
        toAdd.insert(n,1)

        digits.insert(0,0)

        addD = 0
        for i in range(n,-1,-1):
            tmp = toAdd[i] + digits[i] + addD

            result[i] = tmp%10
            addD = tmp/10

        if result[0] == 0:
            result.pop(0)
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.plusOne([0])
    print result
