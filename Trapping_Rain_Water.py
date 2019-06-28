def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    m = -1
    sum = 0
    left = []
    right = []
    h = []
    for i in height:
        if i > m:
            m = i
        left.append(m)
    m = -1
    for i in height[::-1]:
        if i > m:
            m = i
        right.append(m)
    print(right,left)
    left = left[::-1]
    for i in range(len(height)):
        sum += min(left[i],right[i]) - height[i]
    return sum
