class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        n = len(num)
        for i, v in enumerate(num):
            if i == 0:
                if i+1 < n:
                    if num[i] > num[i+1]:
                        return i
                else:
                    return i
            if i == n-1:
                if num[i] > num[i-1]:
                    return i
            if num[i] < num[i-1]:
                continue
            if num[i] > num[i+1]:
                return i
