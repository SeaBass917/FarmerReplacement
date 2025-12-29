import CropType
from movement import go_to

from polycult import handle
handle_polycult = handle

from pumpkin import handle
handle_pumpkin = handle

from cactus import handle
handle_cactus = handle

from sunflower import handle
handle_sunflower = handle

from mazes import handle
handle_mazes = handle

__dispatch_map = {
	CropType.POLY: handle_polycult,
	CropType.PUMPKIN: handle_pumpkin,
	CropType.CACTUS: handle_cactus,
	CropType.SUNFLOWER: handle_sunflower,
	CropType.MAZES: handle_mazes,
}

def dispatch(step):
	x0, y0, _ = step["begin"]
	x1, y1 = step["end"]
	crop_type = step["type"]
	
	# Special cases where we traveling to the start is just pointless
	skip_goto_begin = crop_type == CropType.MAZES and get_entity_type() == Entities.Hedge
	if skip_goto_begin == False:
		go_to(x0, y0)
		
	__dispatch_map[crop_type](step)
	go_to(x1, y1)
