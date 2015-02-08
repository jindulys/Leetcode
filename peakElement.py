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


    # O(lgn) method
    # key point : binary search

    # note 1: if num[mid] > num[mid + 1] we could only consider the half [start, mid]
    # note 2: if num[mid] < num[mid + 1] we could only consider the half [mid + 1, end]

    # pay attention to the edge case:
    # when i==j only 1 element left, must be the answer
    # when i == mid, only 2 elements left, just need to consider the i, j
    # other wise, there at least exists 3 elements

    def findPeakElementLgn(self, num):

        i = 0
        j = len(num)-1
        mid = j/2

        while i < j:
            if mid == i:
                return mid if num[mid] > num[j] else j
            i = i if num[mid] > num[mid + 1] else mid+1
            j = j if num[mid] < num[mid + 1] else mid

            mid = (j+i)/2

        return mid
