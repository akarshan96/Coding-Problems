'''
https://leetcode.com/problems/edit-distance/
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
      

        result = [[0 for x in range(n + 1)] for y in range(m + 1)]

        for i in range(n + 1):
            result[0][i] = i

        for i in range(m + 1):
            result[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word2[i - 1] == word1[j - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = min(result[i - 1][j], result[i][j - 1], result[i - 1][j - 1]) + 1
        return result[-1][-1]
        
