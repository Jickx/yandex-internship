input = [[2, 6], [1, 3], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    prev = intervals[0]
    res = []
    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(interval[1], prev[1])
        else:
            res.append(prev)
            prev = interval
    res.append(prev)
    return res


print(merge(input))
