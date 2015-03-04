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

    def rotate2(self, nums, k):

        if k % len(nums) == 0:
            return

        self.reverse(nums, 0, len(nums) - 1)

        self.reverse(nums, 0, k%len(nums)-1)
        self.reverse(nums, k%len(nums), len(nums)-1)

    # reverse a list from From index to To index
    def reverse(self, nums, From, To):

        while From < To:
            tmp = nums[To]
            nums[To] = nums[From]
            nums[From] = tmp
            From +=1
            To -= 1





def test():
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    s.rotate2(nums,5)
    print "pass" if nums == [5,6,7,8,9,1,2,3,4] else "Fail"

    a = [1,2,3]
    s.reverse(a,0,2)
    print "pass" if a == [3,2,1] else "Fail"

if __name__ == '__main__':
    test()
