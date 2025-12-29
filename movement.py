def go_to(x_target, y_target):
	x_curr, y_curr = None, None
	while x_curr != x_target or y_curr != y_target:
		x_curr, y_curr = get_pos_x(), get_pos_y()
		
		if x_curr < x_target:
			move(East)
		elif x_curr > x_target:
			move(West)
		elif y_curr < y_target:
			move(North)
		elif y_curr > y_target:
			move(South)

# xi, yi = Initial position (Must be on a corner)
# xe, ye = Final position (Must be on a corner)
# dir0 = First step direction (Must be towards another corner)
# x0, y0, x1, y1 = Bounding Rectangle
def plot_route(xi, yi, xe, ye, dir0, x0, y0, x1, y1):
	route = []
	
	# Determine the primary movement direction
	UP_DOWN = 0
	LEFT_RIGHT = 1
	if dir0 in [North, South]:
		pattern = UP_DOWN
		primary_dir = East 
		if xe < xi:
			primary_dir = West
	else:
		pattern = LEFT_RIGHT
		primary_dir = North 
		if ye < yi:
			primary_dir = South
	
	# Walk the route
	x, y = xi, yi
	dir = dir0
	while x != xe or y != ye:
		
		# Different handlers based on pattern
		if pattern == LEFT_RIGHT:

			# Run all the way to the left
			if dir == West:
				while x0 < x:
					route.append(West)
					x -= 1
			elif dir == East:
				while x < x1:
					route.append(East)
					x += 1
			
			# Step up or down
			if y != ye:
				route.append(primary_dir)
				if dir == West:
					dir = East
				else:
					dir = West 
				
				if primary_dir == North:
					y += 1
				else:
					y -= 1

		else:  # UP_DOWN
			
			# Run all the way down
			if dir == South:
				while y0 < y:
					route.append(South)
					y -= 1
			elif dir == North:
				while y < y1:
					route.append(North)
					y += 1
			
			# Step left or right
			if x != xe:
				route.append(primary_dir)
				if dir == North:
					dir = South
				else:
					dir = North 
				
				if primary_dir == East:
					x += 1
				else:
					x -= 1

	
	return route

def after_move(x, y, dir):
	if dir == North:
		return x, y + 1
	elif dir == South:
		return x, y - 1
	elif dir == East:
		return x + 1, y
	elif dir == West:
		return x - 1, y

def reverse_dir(dir):
	dir_flip = {
		North: South,
		South : North,
		East: West,
		West: East,
	}
	return dir_flip[dir]

def reverse_route(route):

	route_reversed = []
	for i in range(len(route) - 1, -1, -1):
		route_reversed.append(reverse_dir(route[i]))

	return route_reversed