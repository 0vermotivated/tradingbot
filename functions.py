def TimeInSec(x):
    return int(x[0:2]) * 3600 + int(x[2:4]) * 60 + int(x[4:6])


def Check(nums, diff, cur):
    n = len(nums)
    s = 0
    for i in range(n):
        s += nums[i]
    s /= n
    if diff * s + s < cur:
        return 1
    elif s - diff * s > cur:
        return 2
    else:
        return 0


def MA(MAnumbers):
    n = len(MAnumbers)
    s = 0
    for i in range(n):
        s += MAnumbers[i]
    return s / n
