class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):

        i = 0
        r = 0
        b = len(A) - 1
        while i <= b:
            if A[i] == 0:
                A[r],A[i] = A[i],A[r]
                r += 1
                i += 1
            elif A[i] == 2:
                A[b],A[i] = A[i],A[b]
                b -= 1
                continue
            else:
                i += 1
