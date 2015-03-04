class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):

        aLen = len(A)-1

        diff = aLen + 1 - (m + n)

        currentA = m-1
        currentB = n-1

        while currentA >= 0 and currentB >= 0:
            if A[currentA] > B[currentB]:
                A[aLen] = A[currentA]
                currentA = currentA - 1
            else:
                A[aLen] = B[currentB]
                currentB -= 1
            aLen -= 1

        while currentA >= 0:
            A[aLen] = A[currentA]
            currentA -= 1
            aLen -= 1

        while currentB >= 0:
            A[aLen] = B[currentB]
            currentB -= 1
            aLen -= 1

        for i in range(m+n):
            A[i] = A[i+diff]
            
