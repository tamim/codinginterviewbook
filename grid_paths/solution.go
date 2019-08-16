func uniquePaths(a int, b int) int {
	grid := make([][]int, a)

	for i := 0; i < a; i++ {
		grid[i] = make([]int, b)
	}

	for i := 0; i < a; i++ {
		grid[i][0] = 1
	}

	for j := 1; j < b; j++ {
		grid[0][j] = 1
	}

	for i := 1; i < a; i++ {
		for j := 1; j < b; j++ {
			grid[i][j] = grid[i-1][j] + grid[i][j-1]
		}
	}

	return grid[a-1][b-1]

}
