class Solution:

    def viable(self,gas, cost):

        if gas == None or cost == None:
            return -1

        if len(gas) ==0 or len(cost) == 0:
            return -1

        stationNumber = len(gas)

        for current in range(len(gas)):
            path = [current]
            remain = gas[current]
            print "This loop index from %d"%(current,)
            while len(path) <= stationNumber:
                top = path[-1]
                remain = remain - cost[top]
                if remain < 0:
                    break
                else:
                    if top == stationNumber - 1:
                        nextStation = 0
                    else:
                        nextStation = top + 1
                    remain += gas[nextStation]
                    path.append(nextStation)
            print "current index is %d the remain is %d"%(current,remain)
            if remain > 0:
                return current

        return -1


if __name__ == "__main__":
    s = Solution()
    gas = [1, 2, 3]
    cost = [2, 4, 0]
    print s.viable(gas, cost)
