class solution:
    # @return a minimum number of candies to return
    def candy(self, ratings):

        n = len(ratings)
        candies = [0]*n
        i = 1
        inc = 1
        while i<n:
            if ratings[i] > ratings[i-1]:
                candies[i] = max(inc, candies[i])
                inc += 1
            else:
                inc = 1
            i += 1

        i = n-2
        inc = 1
        while i >= 0:
            if ratings[i] > ratings[i+1]:
                candies[i] = max(inc, candies[i])
                inc += 1
            else:
                inc = 1
            i -= 1
        return sum(candies)+n







def test(s):
    rating1 = [1,2,3,4,5]
    print "pass %s"%(str(rating1),) if s.candy(rating1) == (1+2+3+4+5) else "fail %s"%(str(rating1),)


    rating2 = [1,5,2,6,9,10,3]
    print "pass %s"%(str(rating2),) if s.candy(rating2) == 14 else "fail %s"%(str(rating2),)

if __name__ == '__main__':
    s = solution()

    test(s)
