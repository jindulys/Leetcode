class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    # Too time consuming, it will require O(k*n) time
    def rotate1(self, nums, k):

        while k > 0:
            tmp = nums[-1]
            count = len(nums) - 1
            while count > 0:
                nums[count] = nums[count - 1]
                count = count -1

            nums[0] = tmp
            k = k -1

    # More good solution, index mapping
    def rotate(self, nums, k):

        if k == 0 or k%len(nums) == 0:
            return

        count = len(nums)
        pre = nums[0]
        idx = 0
        cnt = 0
        for i in range(count):
            tmp = nums[(idx + k)%count]
            nums[(idx + k)%count] = pre
            pre = tmp

            idx = (idx + k)%count
            cnt += k

            if (cnt % count == 0):
                cnt = 0
                idx = idx + 1
                pre = nums[idx]

def test():
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    s.rotate1(nums,5)
    print "pass" if nums == [5,6,7,8,9,1,2,3,4] else "Fail"

if __name__ == '__main__':
    test()
