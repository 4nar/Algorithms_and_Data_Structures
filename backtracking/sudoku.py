'''
Find row, col of an unassigned cell
  If there is none, return true
  For digits from 1 to 9
    a) If there is no conflict for digit at row, col
        assign digit to row, col and recursively try fill in rest of grid
    b) If recursion successful, return true
    c) Else, remove digit and try another
  If all digits have been tried and nothing worked, return false
'''

def safeRowCol(grid, row, col, val):
	for i in range(9):
		if grid[row][i] == val:
			return False 
		elif grid[i][col] == val:
			return False 
	if row%3==0 and col%3==0:
		for i in range(row+1, row+3):
			for j in range(col+1, col+3):
				if grid[i][j] == val:
					return False

	elif row%3==0 and col%3==1:
		for i in range(row+1, row+3):
			for j in range(col-1, col+2, 2):
				if grid[i][j] == val:
					return False

	elif row%3==0 and col%3==2:
		for i in range(row+1, row+3):
			for j in range(col-2, col):
				if grid[i][j] == val:
					return False

	
	elif row%3==1 and col%3==0:
		for i in range(row-1, row+2, 2):
			for j in range(col+1, col+3):
				if grid[i][j] == val:
					return False

	elif row%3==1 and col%3==1:
		for i in range(row-1, row+2, 2):
			for j in range(col-1, col+2, 2):
				if grid[i][j] == val:
					return False
	elif row%3==1 and col%3==2:
		for i in range(row-1, row+2, 2):
			for j in range(col-2, col):
				if grid[i][j] == val:
					return False

	elif row%3==2 and col%3==0:
		for i in range(row-2, row):
			for j in range(col+1, col+3):
				if grid[i][j] == val:
					return False
	elif row%3==2 and col%3==1:
		for i in range(row-2, row):
			for j in range(col-1, col+2, 2):
				if grid[i][j] == val:
					return False
	elif row%3==2 and col%3==2:
		for i in range(row-2, row):
			for j in range(col-2, col):
				if grid[i][j] == val:
					return False


	return True 


def getNextCandidate(grid, start_row):
	for i in range(start_row, 9):
		for j in range(9):
			if grid[i][j]==0:
				return i, j
	return 9, 9
				


def solve(grid, start_row, start_col):
	if start_row>=9 and start_col>=9:
		print('here')
		return True 
	
	
	for val in range(1, 10):
		if safeRowCol(grid, start_row, start_col, val):
			print('val', val)
			grid[start_row][start_col] = val
			print(start_row, start_col)
			printGrid(grid)
			next_row, next_col = getNextCandidate(grid, start_row)
			print('next', next_row, next_col)

			if solve(grid, next_row, next_col):
				return True
			print('setting to 0', start_row, start_col) 
			grid[start_row][start_col] = 0

	return False

def printGrid(grid):
	for i in range(9):
		for j in range(9):
			print(grid[i][j], end=' ')
		print()



if __name__ == '__main__':
	# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
	# 		[5, 2, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 8, 7, 0, 0, 0, 0, 3, 1], 
	# 		[0, 0, 3, 0, 1, 0, 0, 8, 0],
	# 		[9, 0, 0, 8, 6, 3, 0, 0, 5],
	# 		[0, 5, 0, 0, 9, 0, 6, 0, 0],
	# 		[1, 3, 0, 0, 0, 0, 2, 5, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 7, 4],
	# 		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

	grid = [[6, 1, 4, 0, 0, 7, 0, 0, 0],
	 		[0, 0, 8, 0, 0, 0, 9, 0, 1],
	 		[0, 3, 0, 1, 2, 4, 0, 7, 0],
	 		[5, 0, 0, 8, 0, 0, 6, 0, 3],
	 		[0, 9, 2, 0, 0, 0, 1, 5, 0],
	 		[4, 0, 3, 0, 0, 5, 0, 0, 8], 
	 		[0, 8, 0, 3, 9, 2, 0, 6, 0], 
	 		[2, 0, 6, 0, 0, 0, 3, 0, 0], 
	 		[0, 0, 0, 5, 0, 0, 2, 1, 7]]



	# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
	# 		[5, 2, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 8, 7, 0, 0, 0, 0, 3, 1],]		
	init_row, init_col = getNextCandidate(grid, 0)
	status = solve(grid, init_row, init_col)
	print(status)
	printGrid(grid)

