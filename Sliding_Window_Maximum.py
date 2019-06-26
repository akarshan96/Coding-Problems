class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = []
        result = []
        
        for i,val in enumerate(nums):
            if i < k:
                q.append(val)
                if len(q) == k:
                    result.append(max(q))
            else:
                q.pop(0)
                q.append(val)
                result.append(max(q))
        return result

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            line = lines.next()
            k = stringToInt(line)
            
            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
