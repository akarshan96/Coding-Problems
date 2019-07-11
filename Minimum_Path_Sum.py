'''
https://leetcode.com/problems/minimum-path-sum/
Runtime: 80 ms, faster than 83.12% of Python online submissions for Minimum Path Sum.
'''

class Solution(object):
    
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        result = [[0 for x in range(m)] for y in range(n)]
        result[0][0] = grid[0][0]

        for i in range(1,n):
            result[i][0] = result[i - 1][0] + grid[i][0]
        for i in range(1,m):
            result[0][i] = result[0][i - 1] + grid[0][i]
        for i in range(1,n):
            for j in range(1,m):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]

        return(result[n-1][m-1])
