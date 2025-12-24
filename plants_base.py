__water_threshhold = 0.5
__no_soil_enjoyers = [Entities.Grass]

def water():
	if get_water() < __water_threshhold:
		use_item(Items.Water)
		
def do_plant(plant_type, do_water = False, do_fertilizer = False):
	# Ensure soil is what it needs to be
	g_type = get_ground_type()
	is_soil_enjoyer = plant_type not in __no_soil_enjoyers

	# X-or switch when we are the wrong soil
	if is_soil_enjoyer != (g_type == Grounds.Soil):
		till()
	
	# Water if need to
	if do_water:
		water()

	# Plant
	plant(plant_type)
	
	# Fertilize if need to
	if do_fertilizer:
		use_item(Items.Fertilizer)
		