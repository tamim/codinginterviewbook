# https://leetcode.com/problems/insert-interval/

def insert(intervals, new_interval):
    n = len(intervals)
    
    start, end = 0, 0
    while end < n:
        if new_interval[0] <= intervals[end][1]:
            if new_interval[1] < intervals[end][0]:
                break
            new_interval[0] = min(new_interval[0], intervals[end][0])
            new_interval[1] = max(new_interval[1], intervals[end][1])
        else:
            start += 1
        end += 1
    return intervals[:start] + [new_interval] + intervals[end:]


if __name__ == "__main__":
    case_name = "case 1 : insert into an empty interval list"
    intervals = []
    new_interval = [1, 3]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 3]], case_name

    case_name = "case 2 : beginning of the intervals"
    intervals = [[5, 8], [9, 11]]
    new_interval = [1, 3]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 3], [5, 8], [9, 11]], case_name

    case_name = "case 3: end of the intervals"
    intervals = [[5, 8], [9, 11]]
    new_interval = [12, 13]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[5, 8], [9, 11], [12, 13]], case_name

    case_name = "case 4: in-between two intervals"
    intervals = [[1, 5], [9, 11]]
    new_interval = [6, 7]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 5], [6, 7], [9, 11]], case_name

    case_name = "case 5: inside an interval"
    intervals = [[5, 8], [9, 11]]
    new_interval = [6, 8]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[5, 8], [9, 11]], case_name

    case_name = "case 6: all intervals fits inside the new interval"
    intervals = [[5, 8], [9, 11]]
    new_interval = [1, 13]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 13]], case_name

    case_name = "case 7: overlaps with one #1"
    intervals = [[5, 8], [9, 11]]
    new_interval = [1, 6]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 8], [9, 11]], case_name

    case_name = "case 8: overlaps with one #2"
    intervals = [[3, 5], [9, 11]]
    new_interval = [7, 10]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[3, 5], [7, 11]], case_name

    case_name = "case 9: overlaps with two"
    intervals = [[5, 8], [9, 11]]
    new_interval = [7, 10]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[5, 11]], case_name

    case_name = "case 10: overlaps with multiple intervals"
    intervals = [[1, 4], [5, 8], [9, 11], [13, 15]]
    new_interval = [2, 12]
    merged_interval = insert(intervals, new_interval)
    assert merged_interval == [[1, 12], [13, 15]], case_name

    print("done")