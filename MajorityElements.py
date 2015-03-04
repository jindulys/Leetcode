class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dict = {}

        count = len(num)
        for i in range(count):
            if num[i] in dict:
                dict[num[i]] += 1
            else:
                dict[num[i]] = 1

        for k,v in dict.iteritems():
            if v > count/2:
                return k


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):


        count = 1
        major = num[0]

        for i in range(1,len(num)):
            if count == 0:
                count += 1
                major = num[i]
            else:
                if major == num[i]:
                    count += 1
                else:
                    count -= 1
        return major
