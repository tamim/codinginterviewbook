package main

func insert(intervals [][]int, newInterval []int) [][]int {
	n := len(intervals)

	var start, end int
	for end = 0; end < n; end++ {
		if newInterval[0] <= intervals[end][1] {
			if newInterval[1] < intervals[end][0] {
				break
			}
			if intervals[end][0] < newInterval[0] {
				newInterval[0] = intervals[end][0]
			}
			if intervals[end][1] > newInterval[1] {
				newInterval[1] = intervals[end][1]
			}
		} else {
			start++
		}
	}

	var result [][]int
	for i := 0; i < start; i++ {
		result = append(result, intervals[i])
	}
	result = append(result, newInterval)
	for i := end; i < n; i++ {
		result = append(result, intervals[i])
	}

	return result
}

func main() {
	// run the program
}
