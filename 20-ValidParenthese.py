

# according: https://github.com/lilianweng/LeetcodePython/blob/master/valid_parentheses.py
class Solution1:
    # @return a boolean
    def isValid(self, s):
        stack = []

        left = {'(':0,'{':1,'[':2}
        right = {')':0,'}':1,']':2}

        for ch in s:
            if ch in left:
                stack.append(left[ch])
            elif ch in right:
                if not stack: return False
                if stack[-1] == right[ch]: stack.pop()
                else:
                    return False
            else:
                return False
        if not stack: return True
        else: return False

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
