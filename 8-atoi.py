class Solution:
    # @return an integer
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    def atoi(self, str):
        s = str.strip()
        neg = False

        if len(s) == 0:
            return 0

        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        digit = ''
        for ch in s:
            if ch.isdigit():
                digit += ch
            else:
                if len(digit) == 0: return 0
                elif not neg and int(digit) > int('2147483647'): return INT_MAX
                elif neg and int(digit) > int('2147483648'): return INT_MIN
                else:
                    number = int(digit)
                    return -number if neg else number
        if not neg and int(digit) > int('2147483647'): return INT_MAX
        elif neg and int(digit) > int('2147483648'): return INT_MIN
        else:
            number = int(digit)
            return -number if neg else number
def test():
    s = Solution()
    print s.atoi("23a8f")

if __name__ == '__main__':
    test()
