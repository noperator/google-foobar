def answer(food, grid):

	# get min and max cost paths
	def get_x_grid(row, col, mode):

		# if path cost already exists, return it
		if x_grid[row][col][mode]: return x_grid[row][col][mode]

		# get cost of current cell
		cost = grid[row][col]

		# if reached end of path, return cost
		if row == grid_size and col == grid_size: return cost

		# iterate over list comprehension of valid neighboring cells
		for nrow, ncol in [(ncell[0], ncell[1])

			# get neighbors of current cell
			for i, ncell in enumerate([(row+1, col), (row, col+1)])

				# ensure neighbor exists
				if ncell[i]-1 != grid_size

					# ensure cost path at that neighbor has not yet been checked
					and not x_grid[ncell[0]][ncell[1]][mode]]:

						# get cost path for that neighbor
						x_grid[nrow][ncol][mode] = get_x_grid(nrow, ncol, mode)

		# if up against a single border, pursue the opposite path
		if   col == grid_size: cost += x_grid[row+1][col][mode]
		elif row == grid_size: cost += x_grid[row][col+1][mode]

		# if not up against a border, get min/max cost path
		else:
			sign = 1 - 2 * mode
			cost += sign * min(sign * x_grid[row][col+1][mode], sign * x_grid[row+1][col][mode])

		return cost

	# get max cost where cost <= food
	def get_max_cost(row, col, running_cost):

		# add cost of current cell to running path cost
		running_cost += grid[row][col]

		# if reached end of path, return cost
		if row == grid_size and col == grid_size: return running_cost

		# if up against a single border, take the opposite path
		elif col == grid_size: return get_max_cost(row+1, col, running_cost)
		elif row == grid_size: return get_max_cost(row, col+1, running_cost)

		# get adjacent min paths plus running cost
		min_right = get_x_grid(row, col+1, 0) + running_cost
		min_below = get_x_grid(row+1, col, 0) + running_cost

		# get adjacent max paths
		max_right = get_x_grid(row, col+1, 1)
		max_below = get_x_grid(row+1, col, 1)

		# if no valid path exists, return appropriate value
		if min_right > food and min_below > food: return -1

		# if only one path is valid, take that path
		elif min_right > food and min_below <= food: row += 1
		elif min_below > food and min_right <= food: col += 1

		# otherwise, both paths are valid, so take the max cost path
		elif max_right < max_below:	row += 1
		else:                       col += 1

		# pursue path through next cell
		return get_max_cost(row, col, running_cost)

	# cache grid size
	grid_size = len(grid) - 1

	# initialize grid of min/max cost paths
	x_grid = [[[None, None] for x in range(grid_size+1)] for y in range(grid_size+1)]

	# get max valid cost
	max_cost = get_max_cost(0,0,0)

	# return appropriate value
	return food - max_cost if max_cost >= 0 else -1