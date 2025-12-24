from plants_base import do_plant

def process():
	if can_harvest():
		harvest()
	do_plant(Entities.Cactus, False, True)


def handle(step):
	for dir in step["route"]:
		process()
		move(dir)
	process()