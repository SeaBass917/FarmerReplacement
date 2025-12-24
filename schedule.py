import CropType

schedules_map = {
	'schedule_0': [
		{
			'begin': (3, 0, West),
			'rect': (0, 0, 3, 6),
			'type': CropType.POLY,
			'route': [West,West,West,North,East,East,East,North,West,West,West,North,East,East,East,North,West,West,West,North,East,East,East,North,West,West,West],
			'end': (0, 6),
		},
		{
			'begin': (0, 7, North),
			'rect': (0, 7, 10, 11),
			'type': CropType.POLY,
			'route': [North,North,North,North,East,South,South,South,South,East,North,North,North,North,East,South,South,South,South,East,North,North,North,North,East,South,South,South,South,East,North,North,North,North,East,South,South,South,South,East,North,North,North,North,East,South,South,South,South,East,North,North,North,North],
			'end': (10, 11),
		},
		{
			'begin': (11, 11, South),
			'rect': (11, 0, 11, 11),
			'type': CropType.CACTUS,
			'route': [South,South,South,South,South,South,South,South,South,South,South],
			'end': (11, 0),
		},
		{
			'begin': (10, 6, South),
			'rect': (4, 0, 10, 6),
			'type': CropType.PUMPKIN,
			'route': [South,South,South,South,South,South,West,North,North,North,North,North,North,West,South,South,South,South,South,South,West,North,North,North,North,North,North,West,South,South,South,South,South,South,West,North,North,North,North,North,North,West,South,South,South,South,South,South],
			'end': (4, 0),
		}
	],
	'schedule_1': [
		{
			'begin': (7, 0, West),
			'rect': (0, 0, 7, 6),
			'type': CropType.POLY,
			'end': (0, 6),
		},
		{
			'begin': (0, 7, North),
			'rect': (0, 7, 14, 15),
			'type': CropType.POLY,
			'end': (14, 15),
		},
		{
			'begin': (15, 15, South),
			'rect': (15, 0, 15, 15),
			'type': CropType.CACTUS,
			'end': (15, 0),
		},
		{
			'begin': (14, 6, South),
			'rect': (8, 0, 14, 6),
			'type': CropType.PUMPKIN,
			'end': (8, 0),
		}
	],
	'schedule_2': [
		{
			'begin': (0, 0, North),
			'rect': (0, 0, 0, 21),
			'type': CropType.CACTUS,
			'end': (0, 21),
		},
		{
			'begin': (1, 21, South),
			'rect': (1, 6, 8, 21),
			'type': CropType.SUNFLOWER,
			'end': (8, 21),
		},
		{
			'begin': (9, 21, South),
			'rect': (9, 6, 20, 21),
			'type': CropType.POLY,
			'end': (20, 21),
		},
		{
			'begin': (21, 21, South),
			'rect': (21, 0, 21, 21),
			'type': CropType.CACTUS,
			'end': (21, 0),
		},
		{
			'begin': (20, 0, North),
			'rect': (15, 0, 20, 5),
			'type': CropType.PUMPKIN,
			'end': (15, 0),
		},
		{
			'begin': (14, 0, North),
			'rect': (14, 0, 14, 5),
			'type': CropType.POLY,
			'route': [North,North,North,North,North],
			'end': (14, 5),
		},
		{
			'begin': (13, 5, South),
			'rect': (8, 0, 13, 5),
			'type': CropType.PUMPKIN,
			'end': (8, 5),
		},
		{
			'begin': (7, 5, South),
			'rect': (7, 0, 7, 5),
			'type': CropType.POLY,
			'route': [South,South,South,South,South],
			'end': (7, 0),
		},
		{
			'begin': (6, 0, North),
			'rect': (1, 0, 6, 5),
			'type': CropType.PUMPKIN,
			'end': (1, 0),
		}
	],
	'schedule_3': [
		{
			'begin': (1, 6, North),
			'rect': (1, 6, 7, 21),
			'type': CropType.SUNFLOWER,
			'end': (7, 21),
		},
		{
			'begin': (8, 21, South),
			'rect': (8, 16, 13, 21),
			'type': CropType.PUMPKIN,
			'end': (13, 21),
		},
		{
			'begin': (15, 21, South),
			'rect': (15, 16, 20, 21),
			'type': CropType.PUMPKIN,
			'end': (20, 21),
		},
		{
			'begin': (20, 14, South),
			'rect': (15, 9, 20, 14),
			'type': CropType.PUMPKIN,
			'end': (15, 14),
		},
		{
			'begin': (13, 14, South),
			'rect': (8, 9, 13, 14),
			'type': CropType.PUMPKIN,
			'end': (8, 14),
		},
		{
			'begin': (20, 0, North),
			'rect': (15, 0, 20, 5),
			'type': CropType.PUMPKIN,
			'end': (15, 0),
		},
		{
			'begin': (13, 5, South),
			'rect': (8, 0, 13, 5),
			'type': CropType.PUMPKIN,
			'end': (8, 5),
		},
		{
			'begin': (6, 0, North),
			'rect': (1, 0, 6, 5),
			'type': CropType.PUMPKIN,
			'end': (1, 0),
		}
	]
}