from plants_base import do_plant
import state

def plant_carrot():
	if can_harvest(): 
		harvest()
	do_plant(Entities.Carrot, True, True)
	
def plant_tree():
	if can_harvest(): 
		harvest()
	do_plant(Entities.Tree, True, True)
	
def plant_grass():
	harvest()
	do_plant(Entities.Grass, False, True)
	 
def plant_bush():
	if can_harvest(): 
		harvest()
	do_plant(Entities.Bush, False, True)

__plant_map = {
	Entities.Carrot: plant_carrot,
	Entities.Tree: plant_tree,
	Entities.Grass: plant_grass,
	Entities.Bush: plant_bush,
}

def process():
	# Determine what we are going to plant
	x, y = state.get_pos()
	entity = select_crop(x, y)
	
	# Mark bad tree
	state.update_state(x, y, 'immatree', entity == Entities.Tree)

	# Plant the crop
	__plant_map[entity]()

	# Update the preferences map
	preference_handler()


def handle(step):
	for dir in step["route"]:
		process()
		move(dir)
	process()

def select_crop(x, y):
	curr = state.get_state(x, y)

	is_next_to_tree = (x+1 < state.height and state.get_state(x+1, y)['immatree']) or (0 < x and state.get_state(x-1, y)['immatree']) or (y+1 < state.height and state.get_state(x, y+1)['immatree']) or (0 < y and state.get_state(x, y-1)['immatree'])

	entity = curr['preferred']
	if entity and (entity != Entities.Tree or not is_next_to_tree):
		return entity
	
	x = random()
	if x < 0.2 and not is_next_to_tree:
		return Entities.Tree
	elif x < 0.4:
		return Entities.Bush
	elif x < 0.6:
		return Entities.Grass
	else:
		return Entities.Carrot

def preference_handler():
	preferred, (x, y) = get_companion()
	state.update_state(x, y, 'preferred', preferred)
