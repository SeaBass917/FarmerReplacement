import state
from movement import reverse_dir, after_move

def handle(step):
	rect = step["rect"]
	width = rect[2] - rect[0] + 1
	height = rect[3] - rect[1] + 1
	
	# Safety checks
	if width != height:
		print("Error: Maze area must be square!", "Area:", str(width) + "x" + str(height))
		return

	while True:

		# If we are not already in a maze, create one.
		# This is the path we hit if we reset during a run.
		# Don't be wasteful of resources!
		if get_entity_type() != Entities.Hedge:
			subs_needed_cnt = determine_substance_quant(width)
			quick_print("Creating maze of size", str(width) + "x" + str(height), "using", str(subs_needed_cnt), "weird substances.")
			create_maze(subs_needed_cnt)
		else:
			quick_print("Already in a maze, proceeding to solve it.")

		# Solve the maze 
		# (This will harvest the treasure and remove the maze)
		solve_maze(width)

def create_maze(num_substance_to_use):
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, num_substance_to_use)

def determine_substance_quant(size):
	return size * 2**(num_unlocked(Unlocks.Mazes) - 1)

def solve_maze(size):

	# This is our destination
	x_treasure, y_treasure = measure()

	# Keep track of visited cells to avoid loops
	state_matrix = []
	for y in range(size):
		row = []
		for x in range(size):
			row.append({'dead_end': False, 'possible_moves': None, 'visited': False, 'last_move': None})
		state_matrix.append(row)

	# Loop till we find it
	while True:
		x, y = state.get_pos()
		
		# Exit condition
		if (x, y) == (x_treasure, y_treasure):
			quick_print("Reached maze treasure at:", (x, y))
			harvest()
			break

		# Assess the state. What are our options?
		state_curr = state_matrix[y][x]
		state_curr['visited'] = True
		possible_moves = state_curr['possible_moves']
		if possible_moves == None:
			possible_moves = set()
			for dir in [North, East, South, West]:
				x_new, y_new = after_move(x, y, dir)
				if can_move(dir) and state_matrix[y_new][x_new]['visited'] == False:
					possible_moves.add(dir)

			state_curr['possible_moves'] = possible_moves
	
		# Dead end found, flag then backtrack
		if possible_moves == None or len(possible_moves) == 0:
			state_curr['dead_end'] = True
			move(reverse_dir(state_curr['last_move']))
			state_matrix[y][x] = state_curr
			continue

		# Make a move
		dir, remaining_moves = chose_best_move(possible_moves, state_matrix, x, y, x_treasure, y_treasure)
		x_new, y_new = after_move(x, y, dir)
		state_curr['possible_moves'] = remaining_moves
		state_matrix[y_new][x_new]['last_move'] = dir
		move(dir)

		state_matrix[y][x] = state_curr

def chose_best_move(possible_moves, state_matrix, x, y, x_treasure, y_treasure):
	best_dir = None
	best_dist = None
	for dir in possible_moves:
		# Determine new position
		x_new, y_new = after_move(x, y, dir)

		# Check if dead end
		state_next = state_matrix[y_new][x_new]
		if state_next['dead_end']:
			continue

		# Determine distance to treasure
		dist = abs(x_new - x_treasure) + abs(y_new - y_treasure)
		if best_dist == None or dist < best_dist:
			best_dist = dist
			best_dir = dir

	# Remove chosen direction from possible moves
	remaining_moves = set(possible_moves)
	remaining_moves.remove(best_dir)

	return best_dir, remaining_moves