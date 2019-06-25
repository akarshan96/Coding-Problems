'''
https://leetcode.com/problems/decode-ways-ii
135 / 195 test cases passed.
'''
class Solution(object):
    memo = {}
    def numDecodings(self, s):
        """
        :type s: s
        :rtype: int
        """
        if s:
            if s[0] == '0':
                return 0

        if s == '':
            return 1

        if s in self.memo:
            return self.memo[s]
        if s[0] == '*':
            result = self.numDecodings(s[1:]) + 8
        else:
            result = self.numDecodings(s[1:])
        if len(s[:2]) > 1:
            if '*' not in s[:2]:
                if int(s[:2]) < 27:
                    result += Solution().numDecodings(s[2:])
            else:
                sliced_str = s[:2]
                if sliced_str == '**':
                    return 96
            
                else:
                    index = sliced_str.index('*')
                    count = 0
                    for i in range(1, 10):
                        if index == 0:
                            sliced_str = str(i) + sliced_str[1]
                        else:
                            sliced_str = sliced_str[0] + str(i)
                        print(int(sliced_str))
                        if int(sliced_str) < 27:
                            count += 1
                        else:
                            break
                    if index == 1 or sliced_str[0] != 1:
                        count -= 1
                    
                    result = result + Solution().numDecodings(s[2:]) + count

        self.memo[s] = result
        return result
