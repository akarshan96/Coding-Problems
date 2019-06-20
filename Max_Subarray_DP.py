class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []

        for [i, val] in enumerate(arr):
            if i == 0:
                dp.append(arr[0])
            else:
                num = max(dp[-1] + val, val)
                dp.append(num)

        return max(dp)
"""
Runtime: 52 ms, faster than 73.25% of Python online submissions for Maximum Subarray.

Memory Usage: 12.5 MB, less than 25.58% of Python online submissions for Maximum Subarray.

"""

