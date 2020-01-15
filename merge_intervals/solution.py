def merge(intervals):
    intervals.sort()
    n = len(intervals)
    new_intervals = []
    new_intervals.append(intervals[0])
    for i in range(1, n):
        start, end = new_intervals[-1]
        if intervals[i][0] > end:
            new_intervals.append(intervals[i])
        elif intervals[i][1] > end:
            end = intervals[i][1]
            new_intervals[-1] = (start, end)

            
    return new_intervals
    
if __name__ == "__main__":
    intervals = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
    print(merge(intervals))    
