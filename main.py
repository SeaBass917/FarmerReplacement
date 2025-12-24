from movement import plot_route
import router
import state
from schedule import schedules_map

# Main Entry Point
def main():
	height = get_world_size()
	state.create(height)
	
	# Pre-compute each route before we start
	quick_print("Calculating routes...")
	schedule = []
	i = 0
	for stage in schedules_map['schedule_2']:
		if 'route' in stage and stage['route']:
			quick_print('stage', str(i)+")", "Using precomputed route.")
		else:
			quick_print('stage', str(i)+")", "Plotting route...")
		
			xi, yi, dir0 = stage['begin']
			xe, ye = stage['end']
			x0, y0, x1, y1 = stage['rect']
			stage['route'] = plot_route(xi, yi, xe, ye, dir0, x0, y0, x1, y1)

			quick_print('stage', str(i)+")", "Plotted route:", stage['route'])

		schedule.append(stage)
		i += 1

	# Determine what stage of the schedule, if any, we are currently at
	x, y = state.get_pos()
	xi, yi = 0, 0
	stages_0 = None
	stage_index = 0
	for stage in schedule:

		# Check the bounding box
		x0, y0, x1, y1 = stage['rect']
		if x0 <= x <= x1 and y0 <= y <= y1:
			stages_0 = schedule[stage_index:]
			break

		stage_index += 1

	quick_print("Resuming at stage:", stages_0)
	
	# Run the remaining schedule from our current position
	# Note this will be null if we are somewhere that is not on the map.
	# It happens some times
	if stages_0 != None:
		for stage in stages_0:
			quick_print("Processing step:", stage)
			router.dispatch(stage)

	while True:
		for stage in schedule:
			quick_print("Processing step:", stage)
			router.dispatch(stage)

main()
#state.reset()
