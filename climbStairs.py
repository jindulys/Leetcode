class Solution:
    # @param n, an integer
    # @return an integer
    def slowClimbStairs(self, n):

        # Fibonacci Number

        if n == 1:
            return 1
        if n == 2:
            return 2


        return self.slowClimbStairs(n-1) + self.slowClimbStairs(n-2)

    def fastClimbStairs(self, n):

        # use iteration instead of recursion, will improve the performance
        f1 = 1
        f2 = 2

        if n == 1:
            return f1
        if n == 2:
            return f2

        for i in range(3,n+1):
            f1,f2 = f2,f2 + f1
        return f2




if __name__ == "__main__":
    s = Solution()
    print s.slowClimbStairs(10)
    print s.fastClimbStairs(100)
