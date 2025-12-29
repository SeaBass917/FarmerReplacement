import state
from plants_base import do_plant
from movement import go_to, reverse_route
from utils import sort

stopping_count = 100
smallest_petal_cnt = 7

def process():
	if can_harvest():
		harvest()
	do_plant(Entities.Sunflower)

def sow_the_field(route):
	
	# If caches is empty, scan the field
	if state.sunflower_lookup == None:

		measurements = []
		for dir in route:

			# Make sure this is a sunflower here
			if get_entity_type() != Entities.Sunflower:
				harvest()
				do_plant(Entities.Sunflower)

			num_petals = measure()
			x, y = state.get_pos()
			if num_petals == None:
				num_petals = 0
			measurements.append((x, y, num_petals))
			move(dir)

		# Make sure this is a sunflower here
		if get_entity_type() != Entities.Sunflower:
			harvest()
			do_plant(Entities.Sunflower)
		num_petals = measure()
		if num_petals == None:
			num_petals = 0
		x, y = state.get_pos()
		measurements.append((x, y, num_petals))
		
		# Sort the measurements by number of petals
		measurements = sort(measurements, 2, True)

	# Otherwise pull from cache
	else:
		measurements = state.sunflower_lookup

	return measurements

def do_em_all(route):
		
	route_reverse = reverse_route(route)
	for dir in route_reverse:
		harvest()
		move(dir)
	harvest()

def handle(step):
	
	# Scan/sow the route and measure all flowers
	route = step["route"]
	measurements = sow_the_field(route)

	# Pick everything up
	i = 0
	while i < stopping_count:
		x, y, num_petals = measurements.pop(0)

		# If the highest count is the lowest. THen the whole field is empty.
		# Do a fun run where we grab all of em real fast.
		if num_petals == smallest_petal_cnt:
			xe, ye = step['end']
			go_to(xe, ye)
			do_em_all(route)
			sow_the_field(route)
			i+=1
			continue

		go_to(x, y)
		harvest()
		do_plant(Entities.Sunflower, True)
		num_petals = measure()

		# Find the home
		j = 0
		while j < len(measurements):
			_, __, n_petals = measurements[j]
			if n_petals < num_petals:
				j += 1 # Make sure we never place the same spot again
				break
			j += 1
		measurements.insert(j, (x, y, num_petals))

		i += 1
			
	# Cache the measurements
	state.set_sunflower_lookup(measurements)
