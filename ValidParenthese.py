class Solution:
    # @return a boolean
    class Stack():
        def __init__(self):
            self.s = []
            self.sNum = 0

        def isEmpty(self):
            if self.sNum == 0:
                return True
            else:
                return False

        def pop(self):
            if self.isEmpty():
                return None
            else:
               m = self.s[self.sNum - 1]
               del self.s[self.sNum - 1]
               self.sNum -= 1
               return m
        def push(self, data):
            if data == None:
                return

            self.s.append(data)
            self.sNum += 1

        def __str__(self):
            return str(self.s)

    def isValid(self, s):
        stack = self.Stack()
        for i in s:
            if i in '({[':
                stack.push(i)
            else:
                if i == ')':
                    if stack.pop() != '(':
                        return False
                elif i == '}':
                    if stack.pop() != '{':
                        return False
                else:
                    if stack.pop() != '[':
                        return False
        if stack.isEmpty() :
            return True
        else:
            return False

def test():
    s = Solution()
    print 'pass' if s.isValid('()[]{}{}()()') else 'failed'

if __name__ == '__main__':
    test()
