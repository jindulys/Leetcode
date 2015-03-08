import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):

        i = 0
        j = len(s)-1

        while i<j:
            matches =  re.match(r'[\w]',s[i])
            if matches:
                compareLower = matches.group()
            else:
                i += 1
                continue

            matches =  re.match(r'[\w]',s[j])
            if matches:
                compareUpper = matches.group()
            else:
                j -= 1
                continue

            if compareLower.lower() == compareUpper.lower():
                i += 1
                j -= 1
            else:
                return False

        return True
