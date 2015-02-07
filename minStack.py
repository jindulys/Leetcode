class MinStack:
    # @param x, an integer
    # @return an integer



    def __init__(self):
        self.myList = []
        self.topIndex = -1

        self.minIndex = []
        self.minTop = -1

    def push(self, x):
        self.myList.append(x)
        self.topIndex = self.topIndex+1

        if self.minTop == -1:
            self.minIndex.append(self.topIndex)
            self.minTop = self.minTop + 1
        else:
            currentMin = self.minIndex[self.minTop]
            if x < self.myList[currentMin]:
                self.minIndex.append(self.topIndex)
                self.minTop = self.minTop + 1

    # @return nothing
    def pop(self):
        if self.topIndex == self.minIndex[self.minTop]:
            # First remove minIndex
            del self.minIndex[self.minTop]
            self.minTop = self.minTop - 1
        del self.myList[self.topIndex]
        self.topIndex = self.topIndex - 1

    # @return an integer
    def top(self):
        return self.myList[self.topIndex]

    # @return an integer
    def getMin(self):
        min = None
        if self.minTop != -1:
            min = self.myList[self.minIndex[self.minTop]]
        return min

if __name__ == "__main__":
    stack = MinStack()
    stack.push(100)
    stack.push(10)
    stack.push(19)
    stack.push(1)
    stack.push(1001)

    print stack.top() #print 1001
    print stack.getMin() #print 1

    stack.pop()
    stack.pop()

    print stack.getMin() #print 10
