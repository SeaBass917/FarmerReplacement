from plants_base import do_plant

is_all_alive = True

def process():
	global is_all_alive

	is_dead = get_entity_type() != Entities.Pumpkin
	if is_dead:
		is_all_alive = False
		harvest()
		do_plant(Entities.Pumpkin)

def handle(step):
	global is_all_alive
	
	is_all_alive = True
	for dir in step["route"]:
		process()
		move(dir)
	process()
	
	if is_all_alive:
		harvest()
	