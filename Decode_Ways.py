'''
https://leetcode.com/problems/decode-ways/
'''

class Solution(object):
    memo = {}
    def numDecodings(self, str):
        """
        :type s: str
        :rtype: int
        """
        if str:
            if str[0] == '0':
                return 0
        if str == '':
            return 1

        if str in self.memo:
            print self.memo[str]
            return self.memo[str]
        result = Solution().numDecodings(str[1:])
        if len(str[:2]) > 1:
            if int(str[:2]) < 27:
                result += Solution().numDecodings(str[2:])
        self.memo[str] = result
        return result

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().numDecodings(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
