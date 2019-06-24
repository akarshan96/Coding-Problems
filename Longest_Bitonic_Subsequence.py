'''
https://www.interviewbit.com/problems/length-of-longest-subsequence/
Microsoft
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, arr):
        n = len(arr)
        dp = [1] * n
        dp2 = [1] * n
        sum_arr = []
        
        for i in range(n):
            if i == 0:
                continue
            else:
                for j in range(i):
                    if arr[j] < arr[i]:
                        dp[i] = max(dp[i],dp[j] + 1)
        
        for i in range(n - 2, -1 , -1):
            for j in range(n - 1, i , -1):
                    if arr[j] < arr[i]:
                        dp2[i] = max(dp2[i],dp2[j] + 1)
                
        for i in range(n):
            sum_arr.append(dp[i] + dp2[i] - 1)
        if not sum_arr:
            return 0
        return (max(sum_arr))
