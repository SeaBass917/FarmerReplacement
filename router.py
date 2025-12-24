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

__dispatch_map = {
	CropType.POLY: handle_polycult,
	CropType.PUMPKIN: handle_pumpkin,
	CropType.CACTUS: handle_cactus,
	CropType.SUNFLOWER: handle_sunflower,
}

def dispatch(step):
	x0, y0, _ = step["begin"]
	x1, y1 = step["end"]
	
	go_to(x0, y0)
	__dispatch_map[step["type"]](step)
	go_to(x1, y1)
