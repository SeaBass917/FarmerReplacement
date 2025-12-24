state_array = []
height = -1

sunflower_lookup = None

def reset():
	clear()

def create(h):
	global state_array
	global height

	height = h

	state_array = []
	for _ in range(height):
		state_row = []
		for __ in range(height):
			state_row.append({
				"immatree": False,
				"preferred": None,
			})
		state_array.append(state_row)
	return state_array

def get_pos():
	return get_pos_x(), get_pos_y()

def get_state(x = None, y = None):
	if x == None:
		x = get_pos_x()
	if y == None:
		y = get_pos_y()
	return state_array[height - y - 1][x]

def update_state(x, y, state):
	global state_array
	state_array[height - y - 1][x] = state

def update_state(x, y, key, value):
	global state_array
	state_array[height - y - 1][x][key] = value

def set_sunflower_lookup(lookup):
	global sunflower_lookup
	sunflower_lookup = lookup