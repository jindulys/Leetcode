class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):

        if len(A) == 1:
            if A[0] == target:
                return [0,0]
            else:
                return [-1, -1]

        lower = -1
        upper = -1
        n = len(A)
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            # Note: case 1
            if mid < n-1 and A[mid + 1] == target and A[mid] < target:
                lower = mid + 1
                break
            # Note: case 2
            elif A[mid] == target and mid == 0:
                lower = mid
                break
            elif A[mid] < target:
                left = mid + 1
            else:
                # Note contains two case A[mid] > target and A[mid] == target to move left
                right = mid - 1

        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2

            if mid < n-1 and A[mid+1] > target and A[mid] == target:
                upper = mid
                break
            elif A[mid] == target and mid == n-1:
                upper = mid
                break
            elif A[mid] > target:
                right = mid - 1
            else:
                # Note contains two case A[mid] < target and A[mid] == target to move right
                left = mid + 1
        return [lower, upper]

def test():
    s = Solution()
    A1 = [1,2,3,4,5,6,6,6,6,6,7,8,9]
    a1 = s.searchRange(A1, 6)
    print 'pass' if a1 == [5,9] else 'fail'
    a2 = s.searchRange(A1, 100)
    print 'pass' if a2 == [-1, -1] else 'fail'

if __name__ == '__main__':
    test()
